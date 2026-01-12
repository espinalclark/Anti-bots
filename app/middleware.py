from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException

from app.fingerprint import generate_fingerprint
from app.rate_limit import check_rate_limit
from app.scoring import calculate_risk
from app.logger import log_event


class AntiBotMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        ip = request.client.host
        headers = request.headers
        user_agent = headers.get("user-agent", "")

        fingerprint = generate_fingerprint(headers)
        key = f"{ip}:{fingerprint}"

        request_count = check_rate_limit(key)
        score, level = calculate_risk(request_count, user_agent)

        action = "ALLOW"

        if level == "HIGH":
            action = "BLOCK"
            log_event({
                "ip": ip,
                "fingerprint": fingerprint,
                "score": score,
                "level": level,
                "action": action,
                "path": request.url.path
            })
            raise HTTPException(status_code=403, detail="Bot detectado")

        log_event({
            "ip": ip,
            "fingerprint": fingerprint,
            "score": score,
            "level": level,
            "action": action,
            "path": request.url.path
        })

        response = await call_next(request)
        return response

