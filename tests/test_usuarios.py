from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app, raise_server_exceptions=False)


def test_cadastrar_cliente(cleanup_usuario):
    cliente_novo = {
        "email": "lameque@teste.com",
        "senha": "lameque123",
        "nome": "Lameque Usuario Teste",
        "cpf_cnpj": "32735323005",
        "tipo": "PF"
    }
    response = client.post(
        "/usuarios/clientes/cadastrar", 
        json=cliente_novo
    )
    assert response.status_code == 201


def test_cadastrar_administrador(cleanup_admin):
    admin_novo = {
        "email": "robin@teste.com",
        "senha": "robin123",
        "nome": "Robin Administrador Teste",
        "matricula": "1234567",
        "tipo": "ADMINISTRADOR"
    }
    response = client.post(
        "/usuarios/funcionarios/cadastrar", 
        json=admin_novo
    )
    assert response.status_code == 201


def test_cadastrar_mecanico(cleanup_mecanico):
    mecanico_novo = {
        "email": "joao@teste.com",
        "senha": "joao123",
        "nome": "Joao Mecanico Teste",
        "matricula": "7654321",
        "tipo": "MECANICO"
    }
    response = client.post(
        "/usuarios/funcionarios/cadastrar", 
        json=mecanico_novo
    )
    assert response.status_code == 201


def test_login_sucesso(criar_cliente_teste):
    response = client.post(
        "/usuarios/login", 
        data={
            "username": "lameque@teste.com",
            "password": "lameque123"
        } 
    )
    body = response.json()
    assert response.status_code == 200
    assert "access_token" in body
    assert body["token_type"] == "bearer"


def test_login_invalido():
    data = {
        "username": "lameque@teste.com",
        "password": "senha_errada"
    }

    response = client.post("/usuarios/login", data=data)

    assert response.status_code == 401
    assert response.json()["detail"] == "Credenciais inválidas" 
    