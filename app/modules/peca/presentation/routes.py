from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import obter_funcionario_logado
from ..application.use_cases import CriarPecaUseCase, ConsultarPecaUseCase, ListarPecasUseCase, AlterarPecaUseCase, CriarTipoPecaUseCase, ConsultarTipoPecaUseCase, ListarTipoPecasUseCase
from ..application.dto import TipoPecaInputDTO, TipoPecaOutDTO, PecaInputDTO, PecaOutDTO


router = APIRouter()

@router.post("/", response_model=PecaOutDTO)
def criar_peca(dados: PecaInputDTO, db: Session = Depends(get_db), funcionario=Depends(obter_funcionario_logado)):
    use_case = CriarPecaUseCase(db)
    return use_case.execute(dados)


@router.get("/{peca_id}", response_model=PecaOutDTO)
def consultar_peca(peca_id: int, db: Session = Depends(get_db), funcionario=Depends(obter_funcionario_logado)):
    use_case = ConsultarPecaUseCase(db)
    return use_case.execute(peca_id)


@router.put("/{peca_id}", response_model=PecaOutDTO)
def alterar_peca(peca_id: int, dados: PecaInputDTO, db: Session = Depends(get_db), funcionario=Depends(obter_funcionario_logado)):
    use_case = AlterarPecaUseCase(db)
    return use_case.execute(peca_id, dados)


@router.get("/", response_model=list[PecaOutDTO])
def listar_pecas(db: Session = Depends(get_db), funcionario=Depends(obter_funcionario_logado)):
    use_case = ListarPecasUseCase(db)
    return use_case.execute()


@router.post("/tipo-peca", response_model=TipoPecaOutDTO)
def criar_tipo_peca(dados: TipoPecaInputDTO, db: Session = Depends(get_db), funcionario=Depends(obter_funcionario_logado)):
    use_case = CriarTipoPecaUseCase(db)
    return use_case.execute(dados)


@router.get("/tipo-peca/{tipo_peca_id}", response_model=TipoPecaOutDTO)
def consultar_tipo_peca(tipo_peca_id: int, db: Session = Depends(get_db), funcionario=Depends(obter_funcionario_logado)):
    use_case = ConsultarTipoPecaUseCase(db)
    return use_case.execute(tipo_peca_id)


@router.get("/tipo-peca", response_model=list[TipoPecaOutDTO])
def listar_tipo_pecas(db: Session = Depends(get_db), funcionario=Depends(obter_funcionario_logado)):
    use_case = ListarTipoPecasUseCase(db)
    return use_case.execute()
