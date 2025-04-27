from pydantic import BaseModel

class Localizacao(BaseModel):
    id: int
    nome: str
    endereco: str
    cidade: str
    estado: str
    pais: str
    geolocalizacao: str