from dataclasses import dataclass
from datetime import datetime


@dataclass
class Usuario:
    usuario_id: int | None
    email: str
    senha: str
    nome: str
    dta_cadastro: datetime = datetime.now()

@dataclass
class Cliente:
    cliente_id: int | None
    usuario: Usuario
    cpf_cnpj: str
    tipo: str  # 'PF' ou 'PJ'

@dataclass
class Funcionario:
    funcionario_id: int | None
    usuario: Usuario
    matricula: int
    tipo: str  # 'ADMINISTRADOR' ou 'MECANICO'
