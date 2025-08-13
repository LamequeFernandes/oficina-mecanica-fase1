from pydantic import BaseModel


class ClienteInputDTO(BaseModel):
    email: str
    senha: str
    nome: str
    cpf_cnpj: str
    tipo: str = 'PF'


class ClienteOutputDTO(BaseModel):
    cliente_id: int
    nome: str
    email: str


class FuncionarioInputDTO(BaseModel):
    email: str
    senha: str
    nome: str
    matricula: int
    tipo: str = 'FUNCIONARIO'


class FuncionarioOutputDTO(BaseModel):
    funcionario_id: int
    email: str
    nome: str
    matricula: int


from pydantic import BaseModel

class LoginInputDTO(BaseModel):
    username: str
    password: str  


class LoginOutputDTO(BaseModel):
    access_token: str
    token_type: str = 'bearer'
