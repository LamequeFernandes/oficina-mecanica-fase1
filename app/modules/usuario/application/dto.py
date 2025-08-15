from pydantic import BaseModel, validator


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
    cpf_cnpj: str
    tipo: str

    @validator('cpf_cnpj')
    def validar_cpf_cnpj(cls, v):
        if len(v) == 11:
            return f'{v[:3]}.***.***-{v[9:]}'
        return f'{v[:2]}.{v[2:5]}.{v[5:8]}/{v[8:12]}-{v[12:]}'


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
    tipo: str = 'ADMINISTRADOR'


class LoginInputDTO(BaseModel):
    username: str
    password: str


class LoginOutputDTO(BaseModel):
    access_token: str
    token_type: str = 'bearer'
