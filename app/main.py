from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.chat import router as chat_router  # 1. Importa el router de chat

app = FastAPI(
    title="AI Knowledge Assistant",
    version="0.1.0",
)

# Registramos las rutas modulares
app.include_router(health_router)
app.include_router(chat_router)  # 2. Registra el router de chat aquí