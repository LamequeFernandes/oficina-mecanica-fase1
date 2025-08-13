from app.core.security import criar_hash_senha, criar_token_jwt, verificar_senha
from app.modules.usuario.infrastructure.repositories import AuthRepository, ClienteRepository, FuncionarioRepository
from ..domain.entities import Cliente, Usuario, Funcionario
from .dto import ClienteInputDTO, ClienteOutputDTO, FuncionarioInputDTO, FuncionarioOutputDTO, LoginInputDTO, LoginOutputDTO

class CriarClienteUseCase:
    def __init__(self, repo: ClienteRepository):
        self.repo = repo

    def executar(self, dados: ClienteInputDTO) -> ClienteOutputDTO:
        # 1. Hash da senha
        senha_hash = criar_hash_senha(dados.senha)
        
        # 1. Validar CPF (pode usar o Value Object)
        # 2. Criar entidades
        usuario = Usuario(
            usuario_id=None, 
            email=dados.email, 
            senha=senha_hash, 
            nome=dados.nome
        )
        cliente = Cliente(
            cliente_id=None,
            usuario=usuario,
            cpf_cnpj=dados.cpf_cnpj,
            tipo=dados.tipo
        )

        # 3. Persistir
        cliente_salvo = self.repo.salvar(cliente)

        # 4. Retornar DTO de saída
        return ClienteOutputDTO(
            cliente_id=cliente_salvo.cliente_id, # type: ignore
            nome=cliente_salvo.usuario.nome,
            email=cliente_salvo.usuario.email
        )


class CriarFuncionarioUseCase:
    def __init__(self, repo: FuncionarioRepository):
        self.repo = repo

    def executar(self, dados: FuncionarioInputDTO) -> ClienteOutputDTO:
        # 1. Hash da senha
        senha_hash = criar_hash_senha(dados.senha)
        
        # 1. Validar CPF (pode usar o Value Object)
        # 2. Criar entidades
        usuario = Usuario(
            usuario_id=None, 
            email=dados.email, 
            senha=senha_hash, 
            nome=dados.nome
        )
        funcionario = Funcionario(
            funcionario_id=None,
            usuario=usuario,
            matricula=dados.matricula,
            tipo=dados.tipo
        )

        # 3. Persistir
        funcionario_salvo = self.repo.salvar(funcionario)

        # 4. Retornar DTO de saída
        return FuncionarioOutputDTO(
            funcionario_id=funcionario_salvo.funcionario_id, # type: ignore
            nome=funcionario_salvo.usuario.nome,
            email=funcionario_salvo.usuario.email,
            matricula=funcionario.matricula
        )


class LoginUseCase:
    def __init__(self, auth_repo: AuthRepository):
        self.auth_repo = auth_repo

    def execute(self, email: str, senha: str) -> LoginOutputDTO:
        # 1. Buscar usuário por email
        usuario = self.auth_repo.buscar_por_email(email)
        if not usuario:
            raise ValueError("Credenciais inválidas")

        # 2. Verificar senha
        if not verificar_senha(senha, usuario.senha): # type: ignore
            raise ValueError("Credenciais inválidas")

        # 3. Identificar tipo de usuário (Cliente ou Funcionário)
        tipo_usuario = self.auth_repo.obter_tipo_usuario(usuario.usuario_id) # type: ignore

        # 4. Gerar token JWT
        token = criar_token_jwt(usuario.usuario_id)  # type: ignore

        return LoginOutputDTO(access_token=token)
