from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Boolean, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class OrcamentoModel(Base):
    __tablename__ = 'orcamento'

    orcamento_id = Column(Integer, primary_key=True, autoincrement=True)
    status_orcamento = Column(
        Enum('AGUARDANDO_APROVACAO', 'APROVADO', 'CANCELADO', name='status_orcamento'),
        nullable=False
    )
    ordem_servico_id = Column(Integer, ForeignKey('ordem_servico.ordem_servico_id'), nullable=False)
    dta_criacao = Column(DateTime, default=datetime.now)
    dta_cancelamento = Column(DateTime, nullable=True)
    funcionario_id = Column(Integer, ForeignKey('funcionario.funcionario_id'), nullable=False)

    # Relacionamentos
    ordem_servico = relationship("OrdemServicoModel", back_populates="orcamento")
    funcionario = relationship("FuncionarioModel", back_populates="orcamentos")
    servicos = relationship("ServicoModel", back_populates="orcamento")
    pecas = relationship("PecaModel", back_populates="orcamento")


class TipoServicoModel(Base):
    __tablename__ = 'tipo_servico'

    tipo_servico_id = Column(Integer, primary_key=True, autoincrement=True)
    nome_servico = Column(String(255), nullable=False)


class ServicoModel(Base):
    __tablename__ = 'servico'

    servico_id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_servico_id = Column(Integer, ForeignKey('tipo_servico.tipo_servico_id'), nullable=False)
    valor_servico = Column(Numeric(8, 2), nullable=False)
    orcamento_id = Column(Integer, ForeignKey('orcamento.orcamento_id'), nullable=False)

    # Relacionamentos
    tipo_servico = relationship("TipoServicoModel")
    orcamento = relationship("OrcamentoModel", back_populates="servicos")


class TipoPecaModel(Base):
    __tablename__ = 'tipo_peca'

    tipo_peca_id = Column(Integer, primary_key=True, autoincrement=True)
    nome_peca = Column(String(255), nullable=False)
    peca_critica = Column(Boolean, default=False, nullable=False)


class PecaModel(Base):
    __tablename__ = 'peca'

    peca_id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_peca_id = Column(Integer, ForeignKey('tipo_peca.tipo_peca_id'), nullable=False)
    valor_peca = Column(Numeric(8, 2), nullable=False)
    marca = Column(String(255), nullable=False)
    orcamento_id = Column(Integer, ForeignKey('orcamento.orcamento_id'), nullable=True)

    # Relacionamentos
    tipo_peca = relationship("TipoPecaModel")
    orcamento = relationship("OrcamentoModel", back_populates="pecas")
