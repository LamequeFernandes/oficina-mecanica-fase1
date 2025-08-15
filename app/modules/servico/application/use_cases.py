from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.core.exceptions import NaoEncontradoError, ObjetoPossuiVinculoError, ValorDuplicadoError
from app.core.utils import obter_valor_e_key_duplicado_integrity_error

from app.modules.servico.application.dto import ServicoInputDTO, ServicoOutDTO, TipoServicoInputDTO, TipoServicoOutDTO
from app.modules.servico.infrastructure.mapper import ServicoMapper, TipoServicoMapper

from ..domain.entities import Servico, TipoServico
from ..infrastructure.repositories import ServicoRepository, TipoServicoRepository


class CriarServicoUseCase:
    def __init__(self, db: Session):
        self.repo = ServicoRepository(db)

    def execute(self, dados: ServicoInputDTO) -> ServicoOutDTO:
        servico = Servico(
            servico_id=None,
            tipo_servico_id=dados.tipo_servico_id,
            valor_servico=dados.valor_servico
        )
        try:
            servico_salvo = self.repo.salvar(servico)
        except IntegrityError as e:
            valor_duplicado, chave = obter_valor_e_key_duplicado_integrity_error(e)
            raise ValorDuplicadoError(valor_duplicado, chave)
        return ServicoMapper.entity_to_output_dto(servico_salvo)
    

class ConsultarServicoUseCase:
    def __init__(self, db: Session):
        self.repo = ServicoRepository(db)

    def execute(self, servico_id: int) -> ServicoOutDTO | None:
        servico = self.repo.buscar_por_id(servico_id)
        if not servico:
            raise NaoEncontradoError("Serviço", servico_id)
        return ServicoMapper.entity_to_output_dto(servico)


class AlterarServicoUseCase:
    def __init__(self, db: Session):
        self.repo = ServicoRepository(db)

    def execute(self, servico_id: int, dados: ServicoInputDTO) -> ServicoOutDTO:
        servico = self.repo.buscar_por_id(servico_id)
        if not servico:
            raise NaoEncontradoError("Serviço", servico_id)
        servico.tipo_servico_id = dados.tipo_servico_id
        servico.valor_servico = dados.valor_servico
        self.repo.alterar(servico)
        return ServicoMapper.entity_to_output_dto(servico)
    

class RemoverServicoUseCase:
    def __init__(self, db: Session):
        self.repo = ServicoRepository(db)

    def verifica_se_tem_orcamento_vinculado(self, servico: Servico) -> None:
        if servico.orcamento_id:
            raise ObjetoPossuiVinculoError("Serviço", servico.servico_id, "Orçamento") # type: ignore

    def execute(self, servico_id: int) -> None:
        servico = self.repo.buscar_por_id(servico_id)
        if not servico:
            raise NaoEncontradoError("Serviço", servico_id)
        self.verifica_se_tem_orcamento_vinculado(servico)
        self.repo.remover(servico_id)


class CriarTipoServicoUseCase:
    def __init__(self, db: Session):
        self.repo = TipoServicoRepository(db)

    def execute(self, dados: TipoServicoInputDTO) -> TipoServicoOutDTO:
        tipo_servico = TipoServico(
            tipo_servico_id=None,
            nome_servico=dados.nome_servico,
            descricao=dados.descricao
        )
        try:
            tipo_servico_salvo = self.repo.salvar(tipo_servico)
        except IntegrityError as e:
            valor_duplicado, chave = obter_valor_e_key_duplicado_integrity_error(e)
            raise ValorDuplicadoError(valor_duplicado, chave)
        return TipoServicoMapper.entity_to_output_dto(tipo_servico_salvo)


class ConsultarTipoServicoUseCase:
    def __init__(self, db: Session):
        self.repo = TipoServicoRepository(db)

    def execute(self, tipo_servico_id: int) -> TipoServicoOutDTO | None:
        tipo_servico = self.repo.buscar_por_id(tipo_servico_id)
        if not tipo_servico:
            raise NaoEncontradoError("Tipo de Serviço", tipo_servico_id)
        return TipoServicoMapper.entity_to_output_dto(tipo_servico)
    

class ListarTipoServicoUseCase:
    def __init__(self, db: Session):
        self.repo = TipoServicoRepository(db)

    def execute(self) -> list[TipoServicoOutDTO]:
        tipos_servico = self.repo.listar()
        return [TipoServicoMapper.entity_to_output_dto(ts) for ts in tipos_servico]
