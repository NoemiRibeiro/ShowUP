from pydantic import BaseModel
from datetime import date

class Evento(BaseModel):
    id: int
    nome: str
    descricao: str
    tipoDeEvento: str
    statusDoEvento: str
    dataInicio: date
    dataFim: date
    usuarioId: int
    localizacaoId: int