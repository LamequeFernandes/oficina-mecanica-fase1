from sqlalchemy.orm import Session
from ..domain.entities import Cliente, Usuario, Funcionario
from .models import ClienteModel, UsuarioModel, FuncionarioModel
from ..application.interfaces import ClienteRepositoryInterface, FuncionarioRepositoryInterface

class ClienteRepository(ClienteRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def salvar(self, cliente: Cliente) -> Cliente:
        # Converter entidade para modelo ORM
        usuario_model = UsuarioModel(
            email=cliente.usuario.email,
            senha=cliente.usuario.senha,
            nome=cliente.usuario.nome
        )
        cliente_model = ClienteModel(
            cpf_cnpj=cliente.cpf_cnpj,
            tipo_cliente=cliente.tipo,
            usuario=usuario_model
        )

        self.db.add(cliente_model)
        self.db.commit()
        self.db.refresh(cliente_model)

        # Converter de volta para entidade
        return Cliente(
            cliente_id=cliente_model.cliente_id,  # type: ignore
            usuario=Usuario(
                usuario_id=cliente_model.usuario.usuario_id,
                email=cliente_model.usuario.email,
                senha=cliente_model.usuario.senha,
                nome=cliente_model.usuario.nome
            ),
            cpf_cnpj=cliente_model.cpf_cnpj, # type: ignore
            tipo=cliente_model.tipo_cliente # type: ignore
        )

    def buscar_por_cpf(self, cpf: str):
        pass

    def buscar_todos(self):
        pass
    

class FuncionarioRepository(FuncionarioRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def salvar(self, funcionario: Funcionario) -> Funcionario:
        # Converter entidade para modelo ORM
        usuario_model = UsuarioModel(
            email=funcionario.usuario.email,
            senha=funcionario.usuario.senha,
            nome=funcionario.usuario.nome
        )
        funcionario_model = FuncionarioModel(
            matricula=funcionario.matricula,
            tipo_funcionario=funcionario.tipo,
            usuario=usuario_model
        )

        self.db.add(funcionario_model)
        self.db.commit()
        self.db.refresh(funcionario_model)

        # Converter de volta para entidade
        return Funcionario(
            funcionario_id=funcionario_model.funcionario_id,  # type: ignore
            usuario=Usuario(
                usuario_id=funcionario_model.usuario.usuario_id,
                email=funcionario_model.usuario.email,
                senha=funcionario_model.usuario.senha,
                nome=funcionario_model.usuario.nome
            ),
            matricula=funcionario_model.matricula, # type: ignore
            tipo=funcionario_model.tipo_funcionario # type: ignore
        )
    
    def buscar_por_matricula(self, cpf: str):
        pass

    def buscar_todos(self):
        pass


class AuthRepository:
    def __init__(self, db: Session):
        self.db = db

    def buscar_por_email(self, email: str) -> UsuarioModel | None:
        return self.db.query(UsuarioModel).filter(UsuarioModel.email == email).first()

    def obter_tipo_usuario(self, usuario_id: int) -> str:
        # Verifica se é cliente
        cliente = self.db.query(ClienteModel).filter(ClienteModel.usuario_id == usuario_id).first()
        if cliente:
            return "CLIENTE"

        # Verifica se é funcionário
        funcionario = self.db.query(FuncionarioModel).filter(FuncionarioModel.usuario_id == usuario_id).first()
        if funcionario:
            return funcionario.tipo_funcionario  # type: ignore #

        raise ValueError("Usuário não possui perfil associado")
