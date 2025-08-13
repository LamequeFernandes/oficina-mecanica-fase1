
from fastapi import HTTPException, status


class OrdemServicoNotFoundError(Exception):
    """Ordem de serviço não encontrada."""
    def __init__(self, ordem_servico_id: int | None = None):
        super().__init__(f"Ordem de serviço {f'ID {ordem_servico_id}' if ordem_servico_id else ''}não encontrado.")
        self.ordem_servico_id = ordem_servico_id


class VeiculoNotFoundError(Exception):
    """Veículo foi encontrado."""
    def __init__(self, veiculo_id: int | None = None):
        super().__init__(f"Veículo {f'ID {veiculo_id}' if veiculo_id else ''}não encontrado.")
        self.veiculo_id = veiculo_id


class ClienteNotFoundError(Exception):
    """Cliente não encontrado."""
    def __init__(self, cliente_id: int | None = None):
        super().__init__(f"Cliente {f'ID {cliente_id}' if cliente_id else ''}não encontrado.")
        self.cliente_id = cliente_id


class FuncionarioNotFoundError(Exception):
    """Funcionário não encontrado."""
    def __init__(self, funcionario_id: int | None = None):
        super().__init__(f"Funcionário {f'ID {funcionario_id}' if funcionario_id else ''}não encontrado.")
        self.funcionario_id = funcionario_id


class SomenteProprietarioDoUsuarioError(Exception):
    """Somente o proprietário do usuário pode realizar esta ação."""
    def __init__(self):
        super().__init__("Somente o proprietário do usuário pode realizar esta ação.")


class SomenteProprietarioOuAdminError(Exception):
    """Somente o proprietário do usuário ou admin pode realizar esta ação."""
    def __init__(self):
        super().__init__("Somente o proprietário do usuário ou admin pode realizar esta ação.")


class ApenasAdminPodeAcessarError(Exception):
    """Apenas administradores podem acessar."""
    def __init__(self):
        super().__init__("Apenas administradores podem acessar.")


class ApenasMecanicosPodemAcessarError(Exception):
    """Apenas mecanicos podem acessar"""
    def __init__(self):
        super().__init__("Apenas mecanicos podem acessar")


class ApenasClientesPodemAcessarError(Exception):
    """Apenas clientes podem acessar"""
    def __init__(self):
        super().__init__("Apenas clientes podem acessar")


class TokenInvalidoError(Exception):
    """Token inválido ou expirado"""
    def __init__(self):
        super().__init__("Token inválido ou expirado")


class ValidacaoTokenError(Exception):
    """Erro na validação do token"""
    def __init__(self):
        super().__init__("Erro na validação do token")


class TamanhoCPFInvalidoError(Exception):
    """CPF deve ter 11 dígitos numéricos"""
    def __init__(self):
        super().__init__("CPF deve ter 11 dígitos numéricos")


class TamanhoCNPJInvalidoError(Exception):
    """CNPJ deve ter 14 dígitos numéricos"""
    def __init__(self):
        super().__init__("CNPJ deve ter 14 dígitos numéricos")


class TipoInvalidoClienteError(Exception):
    """Tipo de cliente inválido, deve ser PJ ou PF"""
    def __init__(self):
        super().__init__("Tipo de cliente inválido, deve ser PJ ou PF")


class ValorDuplicadoError(Exception):
    """Valor duplicado encontrado."""
    def __init__(self, valor: str, chave: str):
        super().__init__(f"Já existe registro com {chave}={valor}.")
        self.valor = valor
        self.chave = chave


def tratar_erro_dominio(error: Exception) -> HTTPException:
    erros = {
        "status_400": (
            TamanhoCPFInvalidoError,
            TamanhoCNPJInvalidoError,
            TipoInvalidoClienteError,
            ValorDuplicadoError,
        ),
        "status_401": (
            TokenInvalidoError,
            ValidacaoTokenError,
        ),
        "status_403" : (
            ApenasAdminPodeAcessarError,
            ApenasMecanicosPodemAcessarError,
            ApenasClientesPodemAcessarError,
            ClienteNotFoundError,
            FuncionarioNotFoundError,
            SomenteProprietarioDoUsuarioError,
            SomenteProprietarioOuAdminError,
        ),
    }

    if isinstance(error, tuple(erros["status_400"])):
        return HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(error))
    if isinstance(error, tuple(erros["status_401"])):
        return HTTPException(status.HTTP_401_UNAUTHORIZED, detail=str(error))
    if isinstance(error, tuple(erros["status_403"])):
        return HTTPException(status.HTTP_403_FORBIDDEN, detail=str(error))
    return HTTPException(
        status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro interno"
    )
