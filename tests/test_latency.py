import json
import time

from services.gemini_service import generate_response


def test_response_latency():

    with open("datasets/latency_dataset.json") as file:
        dataset = json.load(file)

    for test_data in dataset:

        question = test_data["question"]

        start = time.time()

        generate_response(question)

        end = time.time()

        latency = end - start

        print(f"\nQuestion: {question}")
        print(f"Latency: {latency}")

        assert latency < 5