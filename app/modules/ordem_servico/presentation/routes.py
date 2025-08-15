from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import obter_admin_logado, obter_id_usuario_logado
from ..application.use_cases import CriarOrdemServicoUseCase, ConsultarOrdemServicoUseCase, AlterarStatusOrdemServicoUseCase
from ..application.dto import OrdemServicoAlteracaoStatusInputDTO, OrdemServicoCriacaoInputDTO, OrdemServicoOutputDTO


router = APIRouter()

@router.post("/{veiculo_id}/ordens_servico", response_model=OrdemServicoOutputDTO, status_code=201)
def criar_ordem_servico(
    veiculo_id: int, 
    ordem_servico_data: OrdemServicoCriacaoInputDTO,
    administrador = Depends(obter_admin_logado),  
    db: Session = Depends(get_db),
):
    use_case = CriarOrdemServicoUseCase(db)
    return use_case.execute(veiculo_id, ordem_servico_data) 


@router.get("/{veiculo_id}/ordens_servico/{ordem_servico_id}", response_model=OrdemServicoOutputDTO)
def consultar_ordem_servico(
    veiculo_id: int, 
    ordem_servico_id: int,
    usuario_id = Depends(obter_id_usuario_logado),  
    db: Session = Depends(get_db)
):
    use_case = ConsultarOrdemServicoUseCase(db, usuario_id)
    return use_case.execute(ordem_servico_id)


@router.patch("/{veiculo_id}/ordens_servico/{ordem_servico_id}", response_model=OrdemServicoOutputDTO)
def atualizar_status_ordem_servico(
    veiculo_id: int, 
    ordem_servico_id: int,
    ordem_servico_data: OrdemServicoAlteracaoStatusInputDTO,
    administrador = Depends(obter_admin_logado),  
    db: Session = Depends(get_db),
):
    use_case = AlterarStatusOrdemServicoUseCase(db, administrador.funcionario_id)
    return use_case.execute(ordem_servico_id, ordem_servico_data.status) 
