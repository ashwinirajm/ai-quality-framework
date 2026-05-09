import json

from services.gemini_service import generate_response
from evaluators.relevancy_evaluator import calculate_relevancy


def read_prompt(path):

    with open(path) as file:
        return file.read()


def test_prompt_regression():

    with open("datasets/prompt_regression_dataset.json") as file:
        dataset = json.load(file)

    prompt_v1 = read_prompt("prompts/prompt_v1.txt")
    prompt_v2 = read_prompt("prompts/prompt_v2.txt")

    for test_data in dataset:

        question = test_data["question"]
        expected = test_data["expected_answer"]

        answer_v1 = generate_response(
            question,
            prompt_v1
        )

        answer_v2 = generate_response(
            question,
            prompt_v2
        )

        score_v1 = calculate_relevancy(
            expected,
            answer_v1
        )

        score_v2 = calculate_relevancy(
            expected,
            answer_v2
        )

        print(f"\nQuestion: {question}")
        print(f"V1 Score: {score_v1}")
        print(f"V2 Score: {score_v2}")

        assert score_v2 >= 0.75