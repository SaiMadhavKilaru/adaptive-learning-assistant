
from sklearn.tree import DecisionTreeClassifier

LEVELS = ["Beginner", "Intermediate", "Advanced"]


def build_model():
    X = []
    y = []

    for level in range(3):
        for total in range(1, 4):
            for correct in range(total + 1):
                accuracy = correct / total

                if accuracy >= 2 / 3:
                    next_level = min(level + 1, 2)
                elif accuracy <= 1 / 3:
                    next_level = max(level - 1, 0)
                else:
                    next_level = level

                X.append([level, total, correct])
                y.append(next_level)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)
    return model


MODEL = build_model()


def recommend_level(current_level, history):
    if not history:
        return current_level

    recent = history[-3:]
    total = len(recent)
    correct = sum(recent)

    level_number = LEVELS.index(current_level)

    prediction = MODEL.predict(
        [[level_number, total, correct]]
    )[0]

    return LEVELS[int(prediction)]
