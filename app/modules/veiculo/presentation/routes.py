from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import obter_usuario_logado, obter_cliente_logado
from ..application.use_cases import CriarVeiculoUseCase
from ..application.dto import VeiculoInputDTO


router = APIRouter()

@router.post("/")
def criar_veiculo(
    veiculo_data: VeiculoInputDTO,
    cliente = Depends(obter_cliente_logado), 
    db: Session = Depends(get_db),
):
    use_case = CriarVeiculoUseCase(db)
    return use_case.execute(cliente.cliente_id, veiculo_data) 
