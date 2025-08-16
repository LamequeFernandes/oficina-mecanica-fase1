# 12SOAT - Fase 1 - Tech Challenge

## Identificação

Aluno: Lameque Fernandes Azevedo
Registro FIAP: RM366058

Turma 12SOAT - Software Architecure
Grupo Individual
Grupo 113

Email: lamequesao@gmail.com
Discord: lamequesao

## Descrição
Este projeto é uma API RESTful desenvolvida com FastAPI em Python 3.12, integrada a um banco de dados MySQL. O objetivo principal é fornecer uma aplicação backend para gerenciamento de uma oficina (fase 1), permitindo operações CRUD em entidades relacionadas a veículos, clientes, serviços, peças, orçamentos, ordens de serviço e usuários (incluindo clientes e funcionários). A aplicação segue uma arquitetura limpa (Clean Architecture), com separação em camadas: presentation (rotas), application (use cases e DTOs), domain (entidades e value objects) e infrastructure (repositórios, mappers e models). O projeto é conteinerizado usando Docker Compose.

### Objetivos
- Implementar uma API básica para cadastro, consulta, atualização e exclusão de dados em um banco de dados relacional, com autenticação e autorização.
- Fornecer endpoints seguros para módulos como usuário, veículo, peça, serviço, orçamento e ordem de serviço.
- Utilizar autenticação JWT (com algoritmo HS256) para proteger rotas sensíveis.
- Automatizar a criação das tabelas do banco de dados durante a inicialização do container MySQL.
- Facilitar testes com variáveis de ambiente pré-configuradas.
- Servir como base para fases futuras, como integração com frontend, adição de funcionalidades avançadas (ex.: relatórios, pagamentos) ou escalabilidade.

O projeto assume que o script SQL (`create_db_oficina.sql`) localizado na pasta `scripts/` contém as definições das tabelas e dados iniciais, que são executados automaticamente ao subir o container do banco de dados.

## Requisitos
- Docker e Docker Compose instalados (versão 3.8 ou superior).
- Python 3.12 (para desenvolvimento local, se necessário).
- Bibliotecas Python definidas em `requirements.txt` (instaladas automaticamente via Dockerfile).

## Instalação e Configuração
1. **Clone o repositório**:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd oficina-fase1
   ```

2. **Construa e inicie os containers**:
   Use o Docker Compose para subir os serviços (banco de dados e API).
   ```
   docker-compose up --build
   ```
   - Isso constrói a imagem da API a partir do `Dockerfile`.
   - Inicia o container MySQL (`db`), que cria automaticamente o banco de dados `oficina_fase1` e executa o script SQL para criar as tabelas.
   - Inicia o container da API (`api`), que roda o FastAPI com Uvicorn na porta 8000.

3. **Verifique os logs**:
   - Acesse os logs do container do banco para confirmar a criação das tabelas: `docker logs my-mysql-fase1`.
   - A API estará disponível em `http://localhost:8000`.

4. **Parar os containers**:
   ```
   docker-compose down
   ```

## Variáveis de Ambiente
As variáveis de ambiente são definidas no `Dockerfile` da API para fins de teste e configuração. Elas incluem credenciais do banco de dados e configurações de autenticação JWT. Para produção, recomenda-se usar um gerenciador de segredos (ex.: Docker Secrets ou .env externo).

- `USER_DB`: Usuário do banco de dados (padrão: `lameque`).
- `PASSWORD_DB`: Senha do banco de dados (padrão: `lameque123`).
- `HOST_DB`: Host do banco de dados (padrão: `db` - nome do serviço no Docker Compose).
- `PORT_DB`: Porta do banco de dados (padrão: `3306`).
- `DATABASE`: Nome do banco de dados (padrão: `oficina_fase1`).
- `SECRET_KEY`: Chave secreta para JWT (padrão: `'fc05c7570c34597ddbf3a010cedd9247d5839bd74b6c5f96f770ed4b0f4dc8ff'`).
- `ALGORITHM`: Algoritmo de assinatura JWT (padrão: `HS256`).

Para alterar essas variáveis, edite o `Dockerfile` ou use um arquivo `.env` com `docker-compose --env-file .env up`.

**Nota**: As credenciais do banco de dados no container MySQL são definidas separadamente (`MYSQL_ROOT_PASSWORD=mysqlPW`). Para fins de teste, as variáveis acima são usadas pela API para conectar ao banco.

## Uso
A API é exposta via FastAPI e inclui documentação automática gerada pelo Swagger.

1. **Acesse a documentação da API**:
   - Abra `http://localhost:8000/docs` no navegador.
   - Use o Swagger UI para testar endpoints, autenticar e executar requisições.

2. **Endpoints Principais** (baseados na estrutura de módulos):
   - **Autenticação e Usuários**: Rotas em `usuario/presentation/routes.py`, `routes_clientes.py` e `routes_funcionarios.py` para login, cadastro de usuários, clientes e funcionários.
   - **Veículos**: Rotas em `veiculo/presentation/routes.py` para CRUD de veículos.
   - **Peças**: Rotas em `peca/presentation/routes.py` para gerenciamento de peças.
   - **Serviços**: Rotas em `servico/presentation/routes.py` para serviços oferecidos.
   - **Orçamentos**: Rotas em `orcamento/presentation/routes.py` para criação e gerenciamento de orçamentos.
   - **Ordens de Serviço**: Rotas em `ordem_servico/presentation/routes.py` para ordens de serviço.
   - Exemplos genéricos:
     - POST `/login` - Gera um token JWT.
     - GET `/usuarios` - Lista usuários (protegido por JWT).
     - Consulte os arquivos de rotas para endpoints específicos.

3. **Autenticação**:
   - Use o endpoint de login para obter um token.
   - Inclua o token no header: `Authorization: Bearer <token>`.

4. **Conexão ao Banco de Dados**:
   - As tabelas são criadas automaticamente ao subir o container MySQL via o script em `./scripts/create_db_oficina.sql`.
   - Para acessar o banco manualmente: `docker exec -it my-mysql-fase1 mysql -u root -p` (senha: `mysqlPW`).

## Testes
- **Testes Locais**: Use ferramentas como Postman ou o Swagger UI para testar endpoints.
- **Variáveis para Testes**: As variáveis de ambiente pré-configuradas facilitam testes de integração com o banco. Por exemplo, conecte-se ao banco usando as credenciais `USER_DB` e `PASSWORD_DB` para inserir dados de teste.
- **Testes Automatizados**: Adicione testes unitários/integração em um diretório `tests/` (não incluído nesta fase). Rode com `pytest` (se instalado via `requirements.txt`).
- **Arquivo de Teste**: O arquivo `teste.txt` no root pode ser usado para anotações ou testes manuais.

## Estrutura do Projeto
```
.
├── Dockerfile              # Dockerfile para a API FastAPI
├── app
│   ├── __init__.py         # Inicialização do pacote
│   ├── core                # Configurações centrais (ex.: database, security)
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── exceptions.py
│   │   ├── security.py
│   │   └── utils.py
│   ├── main.py             # Entrypoint da aplicação FastAPI
│   └── modules             # Módulos da API (Clean Architecture)
│       ├── __init__.py
│       ├── orcamento       # Módulo de orçamentos
│       │   ├── __init__.py
│       │   ├── application
│       │   │   ├── dto.py
│       │   │   ├── interfaces.py
│       │   │   └── use_cases.py
│       │   ├── domain
│       │   │   └── entities.py
│       │   ├── infrastructure
│       │   │   ├── mapper.py
│       │   │   ├── models.py
│       │   │   └── repositories.py
│       │   └── presentation
│       │       └── routes.py
│       ├── ordem_servico   # Módulo de ordens de serviço
│       │   ├── __init__.py
│       │   ├── application
│       │   │   ├── __init__.py
│       │   │   ├── dto.py
│       │   │   ├── interfaces.py
│       │   │   └── use_cases.py
│       │   ├── domain
│       │   │   ├── __init__.py
│       │   │   └── entities.py
│       │   ├── infrastructure
│       │   │   ├── __init__.py
│       │   │   ├── mapper.py
│       │   │   ├── models.py
│       │   │   └── repositories.py
│       │   └── presentation
│       │       ├── __init__.py
│       │       └── routes.py
│       ├── peca            # Módulo de peças
│       │   ├── __init__.py
│       │   ├── application
│       │   │   ├── dto.py
│       │   │   ├── interfaces.py
│       │   │   └── use_cases.py
│       │   ├── domain
│       │   │   └── entities.py
│       │   ├── infrastructure
│       │   │   ├── mapper.py
│       │   │   ├── models.py
│       │   │   └── repositories.py
│       │   └── presentation
│       │       └── routes.py
│       ├── servico         # Módulo de serviços
│       │   ├── __init__.py
│       │   ├── application
│       │   │   ├── dto.py
│       │   │   ├── interfaces.py
│       │   │   └── use_cases.py
│       │   ├── domain
│       │   │   └── entities.py
│       │   ├── infrastructure
│       │   │   ├── mapper.py
│       │   │   ├── models.py
│       │   │   └── repositories.py
│       │   └── presentation
│       │       └── routes.py
│       ├── usuario         # Módulo de usuários (clientes e funcionários)
│       │   ├── __init__.py
│       │   ├── application
│       │   │   ├── dto.py
│       │   │   ├── interfaces.py
│       │   │   └── use_cases.py
│       │   ├── domain
│       │   │   ├── entities.py
│       │   │   └── value_objects.py
│       │   ├── infrastructure
│       │   │   ├── mapper.py
│       │   │   ├── models.py
│       │   │   └── repositories.py
│       │   └── presentation
│       │       ├── routes.py
│       │       ├── routes_clientes.py
│       │       └── routes_funcionarios.py
│       └── veiculo         # Módulo de veículos
│           ├── __init__.py
│           ├── application
│           │   ├── dto.py
│           │   ├── interfaces.py
│           │   └── use_cases.py
│           ├── domain
│           │   ├── entities.py
│           │   └── value_objects.py
│           ├── infrastructure
│           │   ├── mapper.py
│           │   ├── models.py
│           │   └── repositories.py
│           └── presentation
│               └── routes.py
├── docker-compose.yml      # Configuração do Docker Compose
├── requirements.txt        # Dependências Python
├── scripts
│   └── create_db_oficina.sql  # Script SQL para criar tabelas e dados iniciais
└── teste.txt               # Arquivo para testes ou anotações
```

## Problemas Comuns e Soluções
- **Erro de Conexão ao Banco**: Verifique se o serviço `db` subiu primeiro (`depends_on` está configurado). Aguarde alguns segundos para o MySQL inicializar.
- **Portas Ocupadas**: Altere as portas em `docker-compose.yml` se 3306 ou 8000 estiverem em uso.
- **Atualizações no Código**: Rebuild a imagem com `docker-compose up --build` após alterações.
