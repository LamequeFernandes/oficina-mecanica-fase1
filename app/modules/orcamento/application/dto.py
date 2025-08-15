from pydantic import BaseModel

from datetime import datetime

from app.modules.orcamento.domain.entities import StatusOrcamento
from app.modules.peca.application.dto import PecaOutDTO
from app.modules.peca.domain.entities import Peca
from app.modules.servico.application.dto import ServicoOutDTO
from app.modules.servico.domain.entities import Servico
from app.modules.usuario.application.dto import FuncionarioOutputDTO
from ...usuario.domain.entities import Funcionario


class OrcamentoInputDTO(BaseModel):
    orcamento_id: int
    funcionario_id: int
    status_orcamento: StatusOrcamento
    dta_criacao: datetime = datetime.now()


class OrcamentoAlteraStatusDTO(BaseModel):
    status_orcamento: StatusOrcamento
    

class OrcamentoOutputDTO(BaseModel):
    orcamento_id: int
    status_orcamento: StatusOrcamento
    valor_total_orcamento: float
    funcionario_id: int
    dta_criacao: datetime
    funcionario_responsavel: FuncionarioOutputDTO
    servicos_inclusos: list[ServicoOutDTO] = []
    pecas_necessarias: list[PecaOutDTO] = []
    dta_cancelamento: datetime | None = None
