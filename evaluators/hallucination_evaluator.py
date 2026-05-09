from evaluators.relevancy_evaluator import calculate_relevancy

def detect_hallucination(context, actual_answer):

    score = calculate_relevancy(
        context,
        actual_answer
    )

    return score