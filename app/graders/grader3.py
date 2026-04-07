def grade_response(response):
    score = 0
    response = response.lower()

    if "refund" in response:
        score += 0.5
    if "sorry" in response:
        score += 0.3
    if "order" in response:
        score += 0.2

    return score