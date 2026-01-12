import hashlib

def generate_fingerprint(headers: dict) -> str:
    user_agent = headers.get("user-agent", "")
    accept_lang = headers.get("accept-language", "")

    raw = f"{user_agent}|{accept_lang}"
    return hashlib.sha256(raw.encode()).hexdigest()

