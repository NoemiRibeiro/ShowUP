from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bem-vindo ao sistema baseado no diagrama de classes!"}


def test_listar_usuarios():
    response = client.get("/usuarios")
    assert response.status_code == 200
    assert response.json() == {"message": "Listando todos os usuários"}


def test_listar_eventos():
    response = client.get("/eventos")
    assert response.status_code == 200
    assert response.json() == {"message": "Listando todos os eventos"}


def test_listar_localizacoes():
    response = client.get("/localizacoes")
    assert response.status_code == 200
    assert response.json() == {"message": "Listando todas as localizações"}


def test_listar_conexoes():
    response = client.get("/conexoes")
    assert response.status_code == 200
    assert response.json() == {"message": "Listando todas as conexões"}
