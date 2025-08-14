from dataclasses import dataclass


@dataclass
class TipoServico:
    tipo_servico_id: int | None
    nome_servico: str
    descricao: str | None


@dataclass
class Servico:
    servico_id: int | None
    tipo_servico: TipoServico
    valor_servico: float
    orcamento_id: int | None

