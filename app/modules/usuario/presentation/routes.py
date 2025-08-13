from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.database import get_db
from ..application.use_cases import CriarClienteUseCase, CriarFuncionarioUseCase, LoginUseCase
from ..application.dto import ClienteInputDTO, ClienteOutputDTO, FuncionarioInputDTO, FuncionarioOutputDTO, LoginOutputDTO, LoginInputDTO
from ..infrastructure.repositories import ClienteRepository, FuncionarioRepository, AuthRepository


router = APIRouter()

@router.post("/clientes/cadastrar", response_model=ClienteOutputDTO)
def criar_cliente(
    cliente_data: ClienteInputDTO,
    db: Session = Depends(get_db)
):
    repo = ClienteRepository(db)
    use_case = CriarClienteUseCase(repo)
    return use_case.executar(cliente_data)


@router.post("/funcionarios/cadastrar", response_model=FuncionarioOutputDTO)
def criar_funcionario(
    funci_data: FuncionarioInputDTO,
    db: Session = Depends(get_db)
):
    repo = FuncionarioRepository(db)
    use_case = CriarFuncionarioUseCase(repo)
    return use_case.executar(funci_data)


# @router.post("/login", response_model=LoginOutputDTO)
# def login(
#     login_data: LoginInputDTO,
#     db: Session = Depends(get_db)
# ):
#     try:
#         repo = AuthRepository(db)
#         use_case = LoginUseCase(repo)
#         return use_case.execute(login_data)
#     except ValueError as e:
#         raise HTTPException(status_code=401, detail=str(e))


@router.post("/login", response_model=LoginOutputDTO)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    try:
        repo = AuthRepository(db)
        use_case = LoginUseCase(repo)
        return use_case.execute(form_data.username, form_data.password) # type: ignore
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
