from enum import StrEnum
from dataclasses import dataclass
from datetime import datetime

from app.modules.peca.domain.entities import Peca
from app.modules.servico.domain.entities import Servico
from ...usuario.domain.entities import Funcionario


class StatusOrcamento(StrEnum):
    AGUARDANDO_APROVACAO = "AGUARDANDO_APROVACAO"
    APROVADO = "APROVADO"
    CANCELADO = "CANCELADO"


@dataclass
class Orcamento:
    orcamento_id: int | None
    funcionario_id: int
    status_orcamento: StatusOrcamento
    ordem_servico_id: int
    funcionario: Funcionario # VER DPS SE PODE SER NULO TODO
    valor_total_orcamento: float | None = None
    dta_criacao: datetime = datetime.now()
    dta_cancelamento: datetime | None = None

    servicos: list[Servico] = []
    pecas: list[Peca] = []

    def __post_init__(self):
        soma_valor_servico = sum(
            servico.valor_servico for servico in self.servicos
        )
        soma_valor_peca = sum(
            peca.valor_peca for peca in self.pecas
        )
        self.valor_total_orcamento = soma_valor_servico + soma_valor_peca
