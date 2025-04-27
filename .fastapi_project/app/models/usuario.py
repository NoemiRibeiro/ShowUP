from datetime import date

from pydantic import BaseModel


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
