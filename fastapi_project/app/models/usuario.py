from pydantic import BaseModel
from datetime import date

class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str
    contato: str
    dataNascimento: str
    bio: str
    dataCadastro: date
    ativo: bool