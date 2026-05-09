import json

from evaluators.hallucination_evaluator import detect_hallucination


def test_hallucination_detection():

    with open("datasets/hallucination_dataset.json") as file:
        dataset = json.load(file)

    for test_data in dataset:

        context = test_data["context"]
        actual_answer = test_data["actual_answer"]

        score = detect_hallucination(
            context,
            actual_answer
        )

        print(f"\nHallucination Score: {score}")

        assert score > 0.75