from pydantic import BaseModel, validator

class Placa(BaseModel):
    valor: str

    @validator('valor')
    def validar_placa(cls, v):
        if len(v) != 7 or not v.isalnum():
            raise ValueError("Placa deve ter 7 caracteres alfanuméricos")
        return v.upper()
