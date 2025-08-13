from sqlalchemy.orm import Session
from app.modules.veiculo.domain.entities import Veiculo
from app.modules.veiculo.infrastructure.models import VeiculoModel
from app.modules.veiculo.application.interfaces import VeiculoRepositoryInterface

class VeiculoRepository(VeiculoRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def salvar(self, cliente_id: int, veiculo: Veiculo) -> Veiculo:
        # Converter entidade para modelo ORM
        veiculo_model = VeiculoModel(
            cliente_id=cliente_id,
            placa=veiculo.placa,
            modelo=veiculo.modelo,
            ano=veiculo.ano
        )

        self.db.add(veiculo_model)
        self.db.commit()
        self.db.refresh(veiculo_model)

        # Converter de volta para entidade
        return Veiculo(
            veiculo_id=veiculo_model.veiculo_id, # type: ignore
            cliente_id=cliente_id,
            placa=veiculo_model.placa, # type: ignore
            modelo=veiculo_model.modelo, # type: ignore
            ano=veiculo_model.ano, # type: ignore
            dta_cadastro=veiculo_model.dta_cadastro, # type: ignore
        )

    def buscar_por_placa(self, cpf: str):
        pass

    def buscar_todos(self):
        pass
    