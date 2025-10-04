from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.core.exceptions import tratar_erro_dominio
from app.modules.usuario.presentation.routes import router as router_usuario
from app.modules.usuario.presentation.routes_clientes import (
    router as router_clientes,
)
from app.modules.usuario.presentation.routes_funcionarios import (
    router as router_funcionarios,
)
from app.modules.veiculo.presentation.routes import router as router_veiculos
from app.modules.orcamento.presentation.routes import (
    router as router_orcamento,
)
from app.modules.ordem_servico.presentation.routes import (
    router as router_ordem_servico,
)
from app.modules.servico.presentation.routes import router as router_servico
from app.modules.peca.presentation.routes import router as router_peca


app = FastAPI(title='Oficina Mecânica - Fase 1', version='1.0.0')


app.include_router(router_usuario, prefix='/usuarios', tags=['Usuários'])
app.include_router(
    router_clientes, prefix='/usuarios/clientes', tags=['Clientes']
)
app.include_router(
    router_funcionarios, prefix='/usuarios/funcionarios', tags=['Funcionários']
)
app.include_router(router_veiculos, prefix='/veiculos', tags=['Veículos'])
app.include_router(router_ordem_servico, tags=['Ordem de Serviço'])
app.include_router(
    router_orcamento, prefix='/veiculos/{veiculo_id}/ordem-servicos', tags=['Orçamento']
)
app.include_router(router_servico, prefix='/servicos', tags=['Serviços'])
app.include_router(router_peca, prefix='/pecas', tags=['Peças'])


@app.exception_handler(Exception)
async def handle_exceptions(request, exc):
    http_exception = tratar_erro_dominio(exc)
    return JSONResponse(
        status_code=http_exception.status_code,
        content={'detail': http_exception.detail},
    )
