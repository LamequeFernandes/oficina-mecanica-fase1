from pydantic import BaseModel, validator

class Email(BaseModel):
    valor: str

    @validator('valor')
    def validar_email(cls, v):
        if '@' not in v:
            raise ValueError('Email inválido')
        return v

class CPF(BaseModel):
    valor: str

    @validator('valor')
    def validar_cpf(cls, v):
        if len(v) != 11 or not v.isdigit():
            raise ValueError('CPF inválido')
        return v