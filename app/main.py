from fastapi import FastAPI, Request
from app.middleware import AntiBotMiddleware

app = FastAPI(
    title="Anti-Bot Security API",
    description="API protegida por un sistema Anti-Bot con Risk Scoring",
    version="1.0.0"
)

app.add_middleware(AntiBotMiddleware)

@app.get("/api/test")
async def test():
    return {
        "status": "ok",
        "message": "Acceso permitido"
    }

@app.post("/login")
async def login(request: Request):
    data = await request.json()

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "admin":
        return {"status": "success"}
    
    return {"status": "error", "message": "Credenciales inválidas"}

