
import unittest

from questions import QUESTIONS
from adaptive_model import recommend_level
from app import new_session, submit_answer, next_question


class TestSmartLearn(unittest.TestCase):

    def test_total_questions(self):
        self.assertEqual(len(QUESTIONS), 30)

    def test_beginner_questions(self):
        self.assertEqual(
            sum(q[0] == "Beginner" for q in QUESTIONS), 10
        )

    def test_intermediate_questions(self):
        self.assertEqual(
            sum(q[0] == "Intermediate" for q in QUESTIONS), 10
        )

    def test_advanced_questions(self):
        self.assertEqual(
            sum(q[0] == "Advanced" for q in QUESTIONS), 10
        )

    def test_start_level(self):
        state = new_session()
        self.assertEqual(state["level"], "Beginner")

    def test_correct_answer(self):
        state = new_session()
        q = QUESTIONS[state["question_id"]]
        answer = q[2][q[3]]

        result = submit_answer(answer, state)
        self.assertEqual(result[0]["correct"], 1)
        self.assertEqual(result[0]["answered"], 1)

    def test_incorrect_answer(self):
        state = new_session()
        q = QUESTIONS[state["question_id"]]
        wrong = q[2][(q[3] + 1) % len(q[2])]

        result = submit_answer(wrong, state)
        self.assertEqual(result[0]["correct"], 0)
        self.assertEqual(result[0]["answered"], 1)

    def test_ai_adapts(self):
        self.assertEqual(
            recommend_level("Beginner", [1]),
            "Intermediate"
        )
        self.assertEqual(
            recommend_level("Advanced", [0]),
            "Intermediate"
        )

    def test_quiz_completion_and_no_repeats(self):
        state = new_session()

        for i in range(10):
            q = QUESTIONS[state["question_id"]]
            answer = q[2][q[3]]
            state = submit_answer(answer, state)[0]

            if i < 9:
                state = next_question(state)[4]

        self.assertEqual(state["answered"], 10)
        self.assertTrue(state["finished"])
        self.assertEqual(len(set(state["used_ids"])), 10)


if __name__ == "__main__":
    unittest.main()
