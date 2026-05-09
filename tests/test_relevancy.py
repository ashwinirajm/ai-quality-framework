import json

from services.gemini_service import generate_response
from evaluators.relevancy_evaluator import calculate_relevancy

def test_ai_response_relevancy():

    with open("datasets/relevancy_dataset.json") as file:
        dataset = json.load(file)

    for test_data in dataset:

        question = test_data["question"]

        expected_answer = test_data["expected_answer"]

        actual_answer = generate_response(question)

        score = calculate_relevancy(
            expected_answer,
            actual_answer
        )

        print("\n-----------------")
        print(f"Question: {question}")
        print(f"Score: {score}")

        assert score > 0.85