from fastapi import APIRouter

router = APIRouter()

@router.get("/localizacoes")
def listar_localizacoes():
    return {"message": "Listando todas as localizações"}