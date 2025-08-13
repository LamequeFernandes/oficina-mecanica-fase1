from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import obter_cliente_logado, obter_id_usuario_logado, obter_usuario_logado
from app.modules.usuario.application.use_cases import AlterarClienteUseCase, AlterarFuncionarioUseCase, ConsultarClienteUseCase, ConsultarFuncionarioUseCase, CriarClienteUseCase, CriarFuncionarioUseCase, LoginUseCase, RemoverClienteUseCase, RemoverFuncionarioUseCase
from app.modules.usuario.application.dto import ClienteInputDTO, ClienteOutputDTO, FuncionarioInputDTO, FuncionarioOutputDTO, LoginOutputDTO
from app.modules.usuario.infrastructure.repositories import AuthRepository


router = APIRouter()

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
    

@router.post("/clientes/cadastrar", response_model=ClienteOutputDTO, status_code=201)
def criar_cliente(
    cliente_data: ClienteInputDTO,
    db: Session = Depends(get_db)
):
    use_case = CriarClienteUseCase(db)
    return use_case.executar(cliente_data)


@router.get("/clientes/{cliente_id}", response_model=ClienteOutputDTO)
def consultar_cliente(
    cliente_id: int,
    usuario_id = Depends(obter_id_usuario_logado), 
    db: Session = Depends(get_db)
):
    use_case = ConsultarClienteUseCase(db)
    return use_case.executar_consulta_por_id(cliente_id)


# TODO: AJUSTAR ENDPOINT
@router.get("/clientes/cpfcnpj/{cpf_cnpj}", response_model=ClienteOutputDTO)
def consultar_cliente_por_cpf_cnpj(
    cpf_cnpj: str,
    usuario_id = Depends(obter_id_usuario_logado), 
    db: Session = Depends(get_db)
):
    use_case = ConsultarClienteUseCase(db)
    return use_case.executar_consulta_por_cpf_cnpj(cpf_cnpj)


@router.put("/clientes/{cliente_id}", response_model=ClienteOutputDTO)
def alterar_cliente(
    cliente_id: int,
    cliente_data: ClienteInputDTO,
    cliente = Depends(obter_cliente_logado), 
    db: Session = Depends(get_db)
):
    use_case = AlterarClienteUseCase(db, cliente)
    return use_case.executar(cliente_id, cliente_data)


@router.delete("/clientes/{cliente_id}", status_code=204)
def remover_cliente(
    cliente_id: int,
    usuario = Depends(obter_usuario_logado), 
    db: Session = Depends(get_db)
):
    use_case = RemoverClienteUseCase(db, usuario)
    use_case.executar(cliente_id)


@router.post("/funcionarios/cadastrar", response_model=FuncionarioOutputDTO, status_code=201)
def criar_funcionario(
    funci_data: FuncionarioInputDTO,
    db: Session = Depends(get_db)
):
    use_case = CriarFuncionarioUseCase(db)
    return use_case.executar(funci_data)


@router.get("/funcionarios/{funcionario_id}", response_model=FuncionarioOutputDTO)
def consultar_funcionario(
    funcionario_id: int,
    usuario_id = Depends(obter_id_usuario_logado), 
    db: Session = Depends(get_db)
):
    use_case = ConsultarFuncionarioUseCase(db)
    return use_case.executar_consulta_por_id(funcionario_id)


# TODO: AJUSTAR ROTA
@router.get("/funcionarios/matricula/{matricula}", response_model=FuncionarioOutputDTO)
def consultar_funcionario_por_matricula(
    matricula: int,
    usuario_id = Depends(obter_id_usuario_logado), 
    db: Session = Depends(get_db)
):
    use_case = ConsultarFuncionarioUseCase(db)
    return use_case.executar_consulta_por_matricula(matricula)


@router.put("/funcionarios/{funcionario_id}", response_model=FuncionarioOutputDTO)
def alterar_funcionario(
    funcionario_id: int,
    funcionario_data: FuncionarioInputDTO,
    usuario = Depends(obter_usuario_logado), 
    db: Session = Depends(get_db)
):
    use_case = AlterarFuncionarioUseCase(db, usuario)
    return use_case.executar(funcionario_id, funcionario_data)


@router.delete("/funcionarios/{funcionario_id}", status_code=204)
def remover_funcionario(
    funcionario_id: int,
    usuario = Depends(obter_usuario_logado), 
    db: Session = Depends(get_db)
):
    use_case = RemoverFuncionarioUseCase(db, usuario)
    use_case.executar(funcionario_id)
