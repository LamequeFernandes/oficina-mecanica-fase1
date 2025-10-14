from fastapi.testclient import TestClient
from app.main import app
from app.modules.orcamento.domain.entities import StatusOrcamento
from app.modules.ordem_servico.domain.entities import StatusOrdemServico

client = TestClient(app, raise_server_exceptions=False)


def test_cadastrar_ordem_servico(obter_ordem_servico, obter_mecanico):
    _, ordem_servico = obter_ordem_servico
    token_mecanico, mecanico = obter_mecanico
    response = client.post(
        f"/veiculos/{ordem_servico.veiculo.veiculo_id}/ordem-servicos/{ordem_servico.ordem_servico_id}/orcamento",
        json={
            "funcionario_id": mecanico.funcionario_id,
            "status_orcamento": StatusOrcamento.AGUARDANDO_APROVACAO.value
        },
        headers={
            "Authorization": f"Bearer {token_mecanico}"
        }
    )
    print(response.json())
    assert response.status_code == 201


def test_buscar_orcamento(obter_orcamento, obter_mecanico):
    _, ordem_servico, orcamento = obter_orcamento
    token_mecanico, _ = obter_mecanico
    response = client.get(
        f"/veiculos/{ordem_servico.veiculo.veiculo_id}/ordem-servicos/{ordem_servico.ordem_servico_id}/orcamento/{orcamento.orcamento_id}",
        headers={
            "Authorization": f"Bearer {token_mecanico}"
        }
    )
    assert response.status_code == 200
    assert response.json()["orcamento_id"] == orcamento.orcamento_id
    assert response.json()["funcionario_id"] == orcamento.funcionario_id
    assert response.json()["valor_total_orcamento"] == orcamento.valor_total_orcamento
    assert response.json()["dta_criacao"] == orcamento.dta_criacao.isoformat()
    assert response.json()["dta_cancelamento"] == orcamento.dta_cancelamento
    assert response.json()["funcionario_responsavel"]["funcionario_id"] == orcamento.funcionario_responsavel.funcionario_id


def test_alterar_status_orcamento(obter_orcamento, obter_mecanico):
    token_cliente, _, ordem_servico, orcamento = obter_orcamento
    response = client.patch(
        f"/veiculos/{ordem_servico.veiculo.veiculo_id}/ordem-servicos/{ordem_servico.ordem_servico_id}/orcamento/{orcamento.orcamento_id}/status",
        json={
            "status_orcamento": StatusOrcamento.APROVADO.value
        },
        headers={
            "Authorization": f"Bearer {token_cliente}"
        }
    )
    assert response.status_code == 200
    # assert response.json()["status_orcamento"] == StatusOrcamento.APROVADO.value

# TO DO
# def test_deletar_orcamento(obter_orcamento, obter_mecanico):
#     _, ordem_servico, orcamento = obter_orcamento
#     token_mecanico, _ = obter_mecanico
#     response = client.delete(
#         f"/veiculos/{ordem_servico.veiculo.veiculo_id}/ordem-servicos/{ordem_servico.ordem_servico_id}/orcamento/{orcamento.orcamento_id}",
#         headers={
#             "Authorization": f"Bearer {token_mecanico}"
#         }
#     )
#     assert response.status_code == 204
