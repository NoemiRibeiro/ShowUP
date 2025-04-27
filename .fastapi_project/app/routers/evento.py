from fastapi import APIRouter

router = APIRouter()


@router.get("/eventos")
def listar_eventos():
    return {"message": "Listando todos os eventos"}
