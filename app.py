
import copy
import gradio as gr

from questions import QUESTIONS
from adaptive_model import recommend_level, LEVELS

MAX_QUESTIONS = 10


def new_session():
    return {
        "question_id": 0,
        "used_ids": [0],
        "level": "Beginner",
        "answered": 0,
        "correct": 0,
        "history": [],
        "waiting": False,
        "finished": False
    }


def display_question(state):
    if state["finished"]:
        return "## Quiz Complete!"

    q = QUESTIONS[state["question_id"]]

    return (
        f"### Question {state['answered'] + 1} "
        f"of {MAX_QUESTIONS}\n\n"
        f"**{q[1]}**"
    )


def display_choices(state):
    return QUESTIONS[state["question_id"]][2]


def display_score(state):
    answered = state["answered"]
    correct = state["correct"]

    accuracy = (
        round(correct / answered * 100, 1)
        if answered else 0
    )

    return (
        f"**Score:** {correct}/{answered}\n\n"
        f"**Accuracy:** {accuracy}%\n\n"
        f"**Difficulty:** {state['level']}\n\n"
        f"**Questions remaining:** {MAX_QUESTIONS - answered}"
    )


def submit_answer(selected, state):
    state = copy.deepcopy(state)

    if state["waiting"] or state["finished"]:
        return (
            state, "Please continue or restart.",
            display_score(state),
            gr.update(interactive=False),
            gr.update(interactive=False),
            gr.update(interactive=not state["finished"])
        )

    if selected is None:
        return (
            state, "⚠️ Please select an answer first.",
            display_score(state),
            gr.update(interactive=True),
            gr.update(interactive=True),
            gr.update(interactive=False)
        )

    q = QUESTIONS[state["question_id"]]
    correct_answer = q[2][q[3]]
    is_correct = selected == correct_answer

    state["answered"] += 1

    if is_correct:
        state["correct"] += 1

    state["history"].append(1 if is_correct else 0)

    state["level"] = recommend_level(
        state["level"], state["history"]
    )

    state["waiting"] = True

    if is_correct:
        feedback = "✅ **Correct answer!**"
    else:
        feedback = (
            f"❌ **Incorrect.** "
            f"Correct answer: **{correct_answer}**"
        )

    feedback += (
        f"\n\n**Explanation:** {q[4]}"
        f"\n\n**AI recommended next level:** {state['level']}"
    )

    if state["answered"] == MAX_QUESTIONS:
        state["finished"] = True
        feedback += (
            f"\n\n## Quiz Complete!"
            f"\n\nFinal score: "
            f"{state['correct']}/{MAX_QUESTIONS}"
        )

    return (
        state,
        feedback,
        display_score(state),
        gr.update(interactive=False),
        gr.update(interactive=False),
        gr.update(interactive=not state["finished"])
    )


def next_question(state):
    state = copy.deepcopy(state)

    if not state["waiting"] or state["finished"]:
        return (
            display_question(state),
            gr.update(),
            "",
            display_score(state),
            state,
            gr.update(interactive=False),
            gr.update(interactive=False)
        )

    recommended = state["level"]

    available = [
        i for i in range(len(QUESTIONS))
        if i not in state["used_ids"]
    ]

    # Prefer unused questions at the recommended level.
    desired = LEVELS.index(recommended)

    available.sort(
        key=lambda i: (
            abs(LEVELS.index(QUESTIONS[i][0]) - desired),
            i
        )
    )

    if not available:
        state["finished"] = True
        return (
            "## Quiz Complete!",
            gr.update(choices=[], value=None),
            "No unused questions remain.",
            display_score(state),
            state,
            gr.update(interactive=False),
            gr.update(interactive=False)
        )

    question_id = available[0]

    state["question_id"] = question_id
    state["used_ids"].append(question_id)
    state["level"] = QUESTIONS[question_id][0]
    state["waiting"] = False

    return (
        display_question(state),
        gr.update(
            choices=display_choices(state),
            value=None,
            interactive=True
        ),
        "",
        display_score(state),
        state,
        gr.update(interactive=True),
        gr.update(interactive=False)
    )


def restart():
    state = new_session()

    return (
        display_question(state),
        gr.update(
            choices=display_choices(state),
            value=None,
            interactive=True
        ),
        "Welcome! Choose an answer to begin.",
        display_score(state),
        state,
        gr.update(interactive=True),
        gr.update(interactive=False)
    )


def create_app():
    with gr.Blocks(title="SmartLearn AI") as demo:

        gr.Markdown(
            "# 🎓 SmartLearn AI\n"
            "## AI-Based Adaptive Learning Assistant\n\n"
            "Learn Computer Science, Python and AI with "
            "questions that adapt to your performance."
        )

        session = gr.State(new_session())

        score = gr.Markdown(
            display_score(new_session())
        )

        question = gr.Markdown(
            display_question(new_session())
        )

        answers = gr.Radio(
            choices=display_choices(new_session()),
            label="Choose your answer"
        )

        with gr.Row():
            submit_btn = gr.Button(
                "Submit Answer",
                variant="primary"
            )

            next_btn = gr.Button(
                "Next Question",
                interactive=False
            )

            restart_btn = gr.Button("Restart Quiz")

        feedback = gr.Markdown(
            "Welcome! Choose an answer to begin."
        )

        submit_btn.click(
            fn=submit_answer,
            inputs=[answers, session],
            outputs=[
                session, feedback, score,
                answers, submit_btn, next_btn
            ]
        )

        next_btn.click(
            fn=next_question,
            inputs=[session],
            outputs=[
                question, answers, feedback,
                score, session, submit_btn, next_btn
            ]
        )

        restart_btn.click(
            fn=restart,
            outputs=[
                question, answers, feedback,
                score, session, submit_btn, next_btn
            ]
        )

        gr.Markdown(
            "---\n"
            "Built with Python, Gradio, and scikit-learn.\n\n"
            "*Educational prototype trained on "
            "synthetic performance examples.*"
        )

    return demo


if __name__ == "__main__":
    app = create_app()
    app.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False
    )
