from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import (
    obter_funcionario_logado,
    obter_mecanico_logado,
)
from app.modules.usuario.infrastructure.models import FuncionarioModel
from app.modules.orcamento.application.use_cases import (
    CriarOrcamentoUseCase,
    BuscarOrcamentoUseCase,
    AlterarStatusOrcamentoUseCase,
    RemoverOrcamentoUseCase,
)
from app.modules.orcamento.application.dto import (
    OrcamentoInputDTO,
    OrcamentoOutputDTO,
    OrcamentoAlteraStatusDTO,
)


router = APIRouter()


@router.post(
    '/{ordem_servico}/orcamento',
    response_model=OrcamentoOutputDTO,
    status_code=201,
)
def criar_orcamento(
    ordem_servico: int,
    dados: OrcamentoInputDTO,
    db: Session = Depends(get_db),
    funcionario_logado: FuncionarioModel = Depends(obter_funcionario_logado),
):
    use_case = CriarOrcamentoUseCase(db)
    return use_case.executar(ordem_servico, dados)


@router.get(
    '/{ordem_servico}/orcamento/{orcamento_id}',
    response_model=OrcamentoOutputDTO,
)
def buscar_orcamento(
    ordem_servico: int,
    orcamento_id: int,
    db: Session = Depends(get_db),
    funcionario_logado: FuncionarioModel = Depends(obter_funcionario_logado),
):
    use_case = BuscarOrcamentoUseCase(db)
    return use_case.executar(orcamento_id)


# @router.patch(
#     '/{ordem_servico}/orcamento/{orcamento_id}/status',
#     response_model=OrcamentoOutputDTO,
# )
# def alterar_status_orcamento(
#     ordem_servico: int,
#     orcamento_id: int,
#     dados: OrcamentoAlteraStatusDTO,
#     db: Session = Depends(get_db),
#     funcionario_logado: FuncionarioModel = Depends(obter_mecanico_logado),
# ):
#     use_case = AlterarStatusOrcamentoUseCase(db, funcionario_logado)
#     return use_case.executar(orcamento_id, dados.status_orcamento)


@router.delete('/{ordem_servico}/orcamento/{orcamento_id}', status_code=204)
def remover_orcamento(
    ordem_servico: int,
    orcamento_id: int,
    db: Session = Depends(get_db),
    funcionario_logado: FuncionarioModel = Depends(obter_mecanico_logado),
):
    use_case = RemoverOrcamentoUseCase(db, funcionario_logado)
    use_case.executar(orcamento_id)
