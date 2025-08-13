from sqlalchemy.orm import Session
from ..domain.entities import OrdemServico
from .dto import OrdemServicoCriacaoInputDTO, OrdemServicoOutputDTO, StatusOrdemServico
from ..infrastructure.mapper import OrdemServicoMapper
from ..infrastructure.repositories import OrdemServicoRepository
from app.core.exceptions import OrdemServicoNotFoundError


class CriarOrdemServicoUseCase:
    def __init__(self, db: Session):
        self.repo = OrdemServicoRepository(db)

    def execute(self, veiculo_id: int, dados: OrdemServicoCriacaoInputDTO) -> OrdemServicoOutputDTO:
        ordem_servico = OrdemServico(
            ordem_servico_id=None,
            veiculo_id=veiculo_id,
            status=StatusOrdemServico.RECEBIDA,
            observacoes=dados.observacoes
        )
        ordem_servico_salva = self.repo.salvar(ordem_servico)

        return OrdemServicoMapper.entity_to_output_dto(ordem_servico_salva)


class AlterarStatusOrdemServicoUseCase:
    def __init__(self, db: Session, usuario_id: int):
        self.repo = OrdemServicoRepository(db)
        self.usuario_id = usuario_id

    def execute(self, ordem_servico_id: int, status: StatusOrdemServico) -> OrdemServicoOutputDTO:
        ordem_servico_atualizada = self.repo.alterar_status(ordem_servico_id, status)
        if not ordem_servico_atualizada:
            raise OrdemServicoNotFoundError
        return OrdemServicoMapper.entity_to_output_dto(ordem_servico_atualizada)


class ConsultarOrdemServicoUseCase:
    def __init__(self, db: Session, usuario_id: int):
        self.repo = OrdemServicoRepository(db)
        self.usuario_id = usuario_id

    def execute(self, ordem_servico_id: int) -> OrdemServicoOutputDTO:
        ordem_servico = self.repo.buscar_por_id(ordem_servico_id)
        if not ordem_servico:
            raise OrdemServicoNotFoundError
        return OrdemServicoMapper.entity_to_output_dto(ordem_servico)
    
