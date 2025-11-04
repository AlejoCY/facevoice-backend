from fastapi import FastAPI
from app.routes import users  # Asegúrate de que importes las rutas de usuario

app = FastAPI()  # Aquí se crea la instancia de FastAPI

# Registrar las rutas en la app
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "API de FaceVoice funcionando 🚀"}