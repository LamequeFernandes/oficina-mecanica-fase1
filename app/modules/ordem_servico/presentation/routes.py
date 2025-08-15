from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import obter_admin_logado, obter_usuario_logado
from ..application.use_cases import CriarOrdemServicoUseCase, ConsultarOrdemServicoUseCase, AlterarStatusOrdemServicoUseCase, RemoverServicoUseCase
from ..application.dto import OrdemServicoAlteracaoStatusInputDTO, OrdemServicoCriacaoInputDTO, OrdemServicoOutputDTO


router = APIRouter()

@router.get("/ordens_servico", response_model=list[OrdemServicoOutputDTO])
def listar_todas_ordens_de_servico(
    usuario_logado = Depends(obter_usuario_logado),  
    db: Session = Depends(get_db)
):
    use_case = ConsultarOrdemServicoUseCase(db, usuario_logado)
    return use_case.execute_listar()


@router.post("/veiculos/{veiculo_id}/ordens_servico", response_model=OrdemServicoOutputDTO, status_code=201)
def criar_ordem_servico(
    veiculo_id: int, 
    ordem_servico_data: OrdemServicoCriacaoInputDTO,
    administrador = Depends(obter_admin_logado),  
    db: Session = Depends(get_db),
):
    use_case = CriarOrdemServicoUseCase(db)
    return use_case.execute(veiculo_id, ordem_servico_data) 


@router.get("/veiculos/{veiculo_id}/ordens_servico/{ordem_servico_id}", response_model=OrdemServicoOutputDTO)
def consultar_ordem_servico(
    veiculo_id: int, 
    ordem_servico_id: int,
    usuario_logado = Depends(obter_usuario_logado),  
    db: Session = Depends(get_db)
):
    use_case = ConsultarOrdemServicoUseCase(db, usuario_logado)
    return use_case.execute_por_id(ordem_servico_id)


@router.get("/veiculos/{veiculo_id}/ordens_servico", response_model=list[OrdemServicoOutputDTO])
def listar_ordens_servico_por_veiculo(
    veiculo_id: int,
    usuario_logado = Depends(obter_usuario_logado),  
    db: Session = Depends(get_db)
):
    use_case = ConsultarOrdemServicoUseCase(db, usuario_logado)
    return use_case.execute_por_veiculo(veiculo_id)


@router.patch("/veiculos/{veiculo_id}/ordens_servico/{ordem_servico_id}", response_model=OrdemServicoOutputDTO)
def atualizar_status_ordem_servico(
    veiculo_id: int, 
    ordem_servico_id: int,
    ordem_servico_data: OrdemServicoAlteracaoStatusInputDTO,
    administrador = Depends(obter_admin_logado),  
    db: Session = Depends(get_db),
):
    use_case = AlterarStatusOrdemServicoUseCase(db, administrador.funcionario_id)
    return use_case.execute(ordem_servico_id, ordem_servico_data.status) 


@router.delete("/veiculos/{veiculo_id}/ordens_servico/{ordem_servico_id}", response_model=OrdemServicoOutputDTO)
def remover_ordem_servico(
    veiculo_id: int, 
    ordem_servico_id: int,
    administrador = Depends(obter_admin_logado),  
    db: Session = Depends(get_db),
):
    use_case = RemoverServicoUseCase(db, administrador)
    use_case.execute(ordem_servico_id)
