from abc import ABC, abstractmethod
from ..domain.entities import Cliente, Funcionario


class ClienteRepositoryInterface(ABC):
    @abstractmethod
    def salvar(self, cliente: Cliente) -> Cliente:
        pass

    @abstractmethod
    def buscar_por_cpf(self, cpf: str) -> Cliente | None:
        pass

    @abstractmethod
    def buscar_todos(self,) -> list[Cliente] | None:
        pass


class FuncionarioRepositoryInterface(ABC):
    @abstractmethod
    def salvar(self, funcionario: Funcionario) -> Funcionario:
        pass

    @abstractmethod
    def buscar_por_matricula(self, cpf: str) -> Funcionario | None:
        pass 

    @abstractmethod
    def buscar_todos(self,) -> list[Funcionario] | None:
        pass
