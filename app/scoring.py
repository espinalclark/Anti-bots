def calculate_risk(
    request_count: int,
    user_agent: str
) -> tuple[int, str]:

    score = 0

    # Rate limiting
    if request_count > 20:
        score += 40
    elif request_count > 10:
        score += 20

    # User-Agent sospechoso
    if not user_agent or "python" in user_agent.lower():
        score += 30

    # Clasificación
    if score >= 60:
        level = "HIGH"
    elif score >= 30:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level

