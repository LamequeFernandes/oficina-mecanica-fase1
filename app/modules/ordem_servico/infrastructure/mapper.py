from app.modules.veiculo.domain.entities import Veiculo
from ..domain.entities import OrdemServico
from ..application.dto import OrdemServicoCriacaoInputDTO, OrdemServicoOutputDTO
from app.modules.veiculo.application.dto import VeiculoOutputDTO
from .models import OrdemServicoModel
from datetime import datetime


class OrdemServicoMapper:
    @staticmethod
    def entity_to_model(ordem_servico: OrdemServico) -> OrdemServicoModel:
        """Converte a Entidade para Modelo ORM."""
        return OrdemServicoModel(
            ordem_servico_id=ordem_servico.ordem_servico_id,
            veiculo_id=ordem_servico.veiculo.veiculo_id, # type: ignore
            status=ordem_servico.status.value,
            obsercacoes=ordem_servico.observacoes,
            dta_criacao=ordem_servico.dta_criacao,
            dta_finalizacao=ordem_servico.dta_finalizacao
        )
    
    @staticmethod
    def model_to_entity(ordem_servico: OrdemServicoModel) -> OrdemServico:
        """Converte o Modelo ORM para Entidade."""
        return OrdemServico(
            ordem_servico_id=ordem_servico.ordem_servico_id, # type: ignore
            veiculo=Veiculo(
                veiculo_id=ordem_servico.veiculo.veiculo_id,
                cliente_id=ordem_servico.veiculo.cliente_id,
                placa=ordem_servico.veiculo.placa,
                modelo=ordem_servico.veiculo.modelo,
                ano=ordem_servico.veiculo.ano,
                dta_cadastro=ordem_servico.veiculo.dta_cadastro
            ),
            status=ordem_servico.status, # type: ignore
            observacoes=ordem_servico.obsercacoes, # type: ignore
            dta_criacao=ordem_servico.dta_criacao, # type: ignore
            dta_finalizacao=ordem_servico.dta_finalizacao # type: ignore
        )
    
    @staticmethod
    def entity_to_output_dto(ordem_servico: OrdemServico) -> OrdemServicoOutputDTO:
        """Converte a Entidade para DTO de Saída."""
        return OrdemServicoOutputDTO(
            ordem_servico_id=ordem_servico.ordem_servico_id, # type: ignore
            veiculo_id=ordem_servico.veiculo_id,
            veiculo=VeiculoOutputDTO(
                veiculo_id=ordem_servico.veiculo.veiculo_id, # type: ignore
                placa=ordem_servico.veiculo.placa, # type: ignore
                modelo=ordem_servico.veiculo.modelo, # type: ignore
                ano=ordem_servico.veiculo.ano, # type: ignore
                cliente_id=ordem_servico.veiculo.cliente_id, # type: ignore
                dta_cadastro=ordem_servico.veiculo.dta_cadastro # type: ignore
            ),
            status=ordem_servico.status,
            dta_criacao=ordem_servico.dta_criacao,
            observacoes=ordem_servico.observacoes,
            dta_finalizacao=ordem_servico.dta_finalizacao
        )
