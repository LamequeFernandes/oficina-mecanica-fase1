from sqlalchemy.orm import Session

from app.modules.veiculo.application.dto import VeiculoInputDTO, VeiculoOutputDTO

from ..domain.entities import Veiculo
from ..infrastructure.repositories import VeiculoRepository

class CriarVeiculoUseCase:
    def __init__(self, db: Session):
        self.repo = VeiculoRepository(db)

    def execute(self, cliente_id: int, dados: VeiculoInputDTO) -> VeiculoOutputDTO:
        veiculo = Veiculo(
            veiculo_id=None,
            cliente_id=cliente_id,  # Associa ao cliente autenticado
            placa=dados.placa,
            modelo=dados.modelo,
            ano=dados.ano,
        )
        veiculo_salvo = self.repo.salvar(cliente_id, veiculo)
        
        return VeiculoOutputDTO(
            veiculo_id=veiculo_salvo.veiculo_id, # type: ignore
            placa=veiculo_salvo.placa,
            modelo=veiculo_salvo.modelo,
            ano=veiculo_salvo.ano,
            cliente_id=veiculo_salvo.cliente_id,
            dta_cadastro=veiculo_salvo.dta_cadastro,
        )
