from abc import ABC, abstractmethod
from app.modules.peca.domain.entities import Peca, TipoPeca


class PecaRepositoryInterface(ABC):
    @abstractmethod
    def salvar(self, peca: Peca) -> Peca:
        pass

    @abstractmethod
    def buscar_por_id(self, peca_id: int) -> Peca | None:
        pass

    @abstractmethod
    def alterar(self, peca: Peca) -> Peca:
        pass


class TipoPecaRepositoryInterface(ABC):
    @abstractmethod
    def salvar(self, tipo_peca: TipoPeca) -> TipoPeca:
        pass

    @abstractmethod
    def buscar_por_id(self, tipo_peca_id: int) -> TipoPeca | None:
        pass

    @abstractmethod
    def listar(self) -> list[TipoPeca]:
        pass

