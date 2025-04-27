from fastapi import APIRouter

router = APIRouter()


@router.get("/conexoes")
def listar_conexoes():
    return {"message": "Listando todas as conexões"}
