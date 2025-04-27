from pydantic import BaseModel


class Conexao(BaseModel):
    id: int
    emissorConvite: int
    recepitorConvite: int
    evento: int
    aceite: bool
