def judge(question, expects, answer, results) -> bool:
    """
    q: 'give', expect : 'give'
    the expect is in the answer

    """

    return expects.lower().strip() in answer.lower()

    """
    LLM as judge
    rapidfuzz
    """


def retrieval_hits(expected, results) -> bool:
    """"
    any part of my expects is the result
    """

    return any(expects.strip().lower() in chunk.lower() for chunk in results)