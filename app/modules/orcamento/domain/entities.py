from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from ...ordem_servico.domain.entities import OrdemServico
# from ...usuario.domain.entities import Funcionario

class StatusOrcamento(Enum):
    AGUARDANDO_APROVACAO = "AGUARDANDO_APROVACAO"
    APROVADO = "APROVADO"
    CANCELADO = "CANCELADO"

@dataclass
class Orcamento:
    orcamento_id: int | None
    ordem_servico: OrdemServico
    status: StatusOrcamento
    dta_criacao: datetime = datetime.now()
    dta_cancelamento: datetime | None = None
    funcionario: Funcionario  # Quem criou o orçamento
