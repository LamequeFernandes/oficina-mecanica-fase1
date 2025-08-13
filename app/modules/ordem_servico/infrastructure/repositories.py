from sqlalchemy.orm import Session
from app.modules.ordem_servico.application.dto import OrdemServicoCriacaoInputDTO
from app.modules.ordem_servico.domain.entities import OrdemServico, StatusOrdemServico
from app.modules.veiculo.domain.entities import Veiculo
from app.modules.ordem_servico.infrastructure.models import OrdemServicoModel
from app.modules.ordem_servico.application.interfaces import OrdemServicoRepositoryInterface
from app.modules.ordem_servico.infrastructure.mapper import OrdemServicoMapper


class OrdemServicoRepository(OrdemServicoRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def salvar(self, dados: OrdemServico) -> OrdemServico:
        ordem_servico_model = OrdemServicoModel(
            veiculo_id=dados.veiculo_id,
            status=dados.status,
            obsercacoes=dados.observacoes
        )

        self.db.add(ordem_servico_model)
        self.db.commit()
        self.db.refresh(ordem_servico_model)

        return OrdemServicoMapper.model_to_entity(ordem_servico_model)


    def buscar_por_id(self, ordem_servico_id: int) -> OrdemServico | None:
        ordem_servico = self.db.query(OrdemServicoModel).filter(
            OrdemServicoModel.ordem_servico_id == ordem_servico_id
        ).first()

        if not ordem_servico:
            return None
        return OrdemServicoMapper.model_to_entity(ordem_servico)


    def buscar_por_veiculo(self, veiculo_id: int) -> list[OrdemServico] | None:
        ordens_servico = self.db.query(OrdemServicoModel).filter(
            OrdemServicoModel.veiculo_id == veiculo_id
        ).all()

        if not ordens_servico:
            return None
        return [
            OrdemServicoMapper.model_to_entity(ordem_servico)
            for ordem_servico in ordens_servico
        ]


    def alterar_status(
        self, ordem_servico_id: int, status: StatusOrdemServico
    ) -> OrdemServico | None:
        ordem_servico = self.db.query(OrdemServicoModel).filter(OrdemServicoModel.ordem_servico_id==ordem_servico_id).first()

        ordem_servico.status = status.value  # type: ignore
        self.db.commit()
        self.db.refresh(ordem_servico)

        return OrdemServicoMapper.model_to_entity(ordem_servico)
    

    def buscar_por_cliente(self, cliente_id: int) -> OrdemServico | None:
        pass
