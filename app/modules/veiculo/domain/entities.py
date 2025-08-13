from dataclasses import dataclass
from datetime import datetime
from ...usuario.domain.entities import Cliente  # Importa a entidade Cliente

@dataclass
class Veiculo:
    veiculo_id: int | None
    # cliente: Cliente  # Relacionamento com Cliente
    cliente_id: int
    placa: str
    modelo: str
    ano: int
    dta_cadastro: datetime = datetime.now()
