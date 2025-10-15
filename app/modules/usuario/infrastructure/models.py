from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship

from app.core.database import Base


class UsuarioModel(Base):
    __tablename__ = 'usuario'

    usuario_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
    nome = Column(String(255), nullable=False)
    dta_cadastro = Column(DateTime, default=datetime.now)

    # Relacionamentos
    cliente = relationship(
        'ClienteModel', back_populates='usuario', uselist=False
    )
    funcionario = relationship(
        'FuncionarioModel', back_populates='usuario', uselist=False
    )


class ClienteModel(Base):
    __tablename__ = 'cliente'

    cliente_id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(
        Integer, ForeignKey('usuario.usuario_id'), unique=True, nullable=False
    )
    cpf_cnpj = Column(String(14), unique=True, nullable=False)
    tipo_cliente = Column(
        Enum('PF', 'PJ', name='tipo_cliente'), nullable=False
    )

    # Relacionamentos
    usuario = relationship('UsuarioModel', back_populates='cliente')
    veiculos = relationship('VeiculoModel', back_populates='cliente')


class FuncionarioModel(Base):
    __tablename__ = 'funcionario'

    funcionario_id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(
        Integer, ForeignKey('usuario.usuario_id'), unique=True, nullable=False
    )
    matricula = Column(Integer, unique=True, nullable=False)
    tipo_funcionario = Column(
        Enum('ADMINISTRADOR', 'MECANICO', name='tipo_funcionario'),
        nullable=False,
    )

    # Relacionamentos
    usuario = relationship('UsuarioModel', back_populates='funcionario')
    orcamentos = relationship('OrcamentoModel', back_populates='funcionario')
