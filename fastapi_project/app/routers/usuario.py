from fastapi import APIRouter

router = APIRouter()

@router.get("/usuarios")
def listar_usuarios():
    return {"message": "Listando todos os usuários"}