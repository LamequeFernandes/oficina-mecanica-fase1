from abc import ABC, abstractmethod
from app.modules.veiculo.domain.entities import Veiculo


class VeiculoRepositoryInterface(ABC):
    @abstractmethod
    def salvar(self, veiculo: Veiculo) -> Veiculo:
        pass

    @abstractmethod
    def buscar_por_placa(self, placa: str) -> Veiculo | None:
        pass

