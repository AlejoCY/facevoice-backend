from fastapi import APIRouter

# Define el router
router = APIRouter(prefix="/api/users", tags=["Users"])

# Define una ruta de ejemplo
@router.get("/")
def get_users():
    return {"message": "Ruta de usuarios funcionando ✅"}