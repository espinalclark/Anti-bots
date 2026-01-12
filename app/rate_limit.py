import time

# Simulación en memoria (luego Redis)
RATE_LIMIT = {}
WINDOW = 60        # segundos
MAX_REQUESTS = 20  # por ventana

def check_rate_limit(key: str) -> int:
    now = time.time()
    window_start = now - WINDOW

    requests = RATE_LIMIT.get(key, [])
    requests = [t for t in requests if t > window_start]

    requests.append(now)
    RATE_LIMIT[key] = requests

    return len(requests)

