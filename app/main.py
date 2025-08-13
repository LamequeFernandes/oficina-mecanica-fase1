from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.core.database import get_db, Base, engine
# from app.core.security import criar_hash_senha

from app.core.exceptions import tratar_erro_dominio
from app.modules.usuario.presentation.routes import router as router_usuario
from app.modules.veiculo.presentation.routes import router as router_veiculos
from app.modules.ordem_servico.presentation.routes import router as router_ordem_servico

app = FastAPI()

# Cria as tabelas (apenas para desenvolvimento)
from app.modules.usuario.infrastructure.models import *
from app.modules.veiculo.infrastructure.models import *
from app.modules.ordem_servico.infrastructure.models import *
from app.modules.orcamento.infrastructure.models import *

Base.metadata.create_all(engine)

app.include_router(router_usuario, prefix='/usuarios', tags=['Usuários'])
app.include_router(router_veiculos, prefix='/veiculos', tags=['Veículos'])
app.include_router(router_ordem_servico, prefix='/veiculo', tags=['Ordem de Serviço'])


# @app.exception_handler(Exception)
# async def handle_exceptions(request, exc):
#     return tratar_erro_dominio(exc)

@app.exception_handler(Exception)
async def handle_exceptions(request, exc):
    http_exception = tratar_erro_dominio(exc)
    return JSONResponse(
        status_code=http_exception.status_code,
        content={"detail": http_exception.detail}
    )
