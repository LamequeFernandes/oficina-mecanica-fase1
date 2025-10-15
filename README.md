# 12SOAT - Fase 2 - Tech Challenge

## Identificação

**Aluno:** Lameque Fernandes Azevedo
**Registro FIAP:** RM366058
**Turma:** 12SOAT – Software Architecture
**Grupo:** Individual (83)
**Email:** [lamequesao@gmail.com](mailto:lamequesao@gmail.com)
**Discord:** lamequesao

---

## Descrição do Projeto

Este projeto é uma **API RESTful** desenvolvida em **Python 3.12** com **FastAPI**, integrada a um banco de dados **MySQL**.
Seu objetivo é fornecer uma aplicação backend para o **gerenciamento de uma oficina**, permitindo CRUD completo sobre entidades como **usuários, clientes, veículos, peças, serviços, orçamentos e ordens de serviço**.

A arquitetura segue os princípios da **Clean Architecture**, com camadas bem definidas:

* **Presentation** → Rotas e controladores (FastAPI)
* **Application** → Casos de uso, interfaces e DTOs
* **Domain** → Entidades e regras de negócio
* **Infrastructure** → Persistência, repositórios e mapeamento ORM

A solução é **totalmente conteinerizada com Docker**, possui **infraestrutura gerenciada via Terraform (AWS)** e **deploy automatizado via GitHub Actions para o EKS (Kubernetes)**.

---

## Arquitetura da Solução

Desenho da arquitetura proposta:
![](docs/architecture_diagram.png)

### Componentes Principais

* **FastAPI Application**: API principal (Backend)
* **MySQL (RDS AWS)**: Banco de dados relacional gerenciado
* **AWS EKS (Kubernetes)**: Orquestração dos containers
* **AWS S3 (opcional)**: Armazenamento de objetos (futuras fases)
* **GitHub Actions**: CI/CD (Build → Test → Deploy)
* **Terraform**: Provisionamento de infraestrutura (VPC, RDS, EKS)

### Fluxo de Deploy

1. **Desenvolvedor** faz push no branch `main`.
2. **GitHub Actions** executa:

   * Build da imagem Docker e push para o **Docker Hub**.
   * Execução dos **testes automatizados** em ambiente isolado (MySQL container).
   * Criação/atualização dos **Secrets** no cluster.
   * Deploy automatizado no **EKS**.
3. **Kubernetes** aplica:

   * `ConfigMap` com variáveis de ambiente.
   * `Secret` com credenciais seguras.
   * `Deployment` com nova imagem da API.
   * `Service` expondo a API no cluster.
   * `HPA` para autoescalonamento.

*(O diagrama de arquitetura está disponível na pasta `docs/architecture_diagram.png`.)*

---

## Execução Local

### Pré-requisitos

* [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/)
* Python 3.12+ (apenas se for rodar localmente fora do Docker)

### Passos

1. **Clone o repositório**

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd oficina-fase1
   ```

2. **Suba os containers**

   ```bash
   docker-compose up --build
   ```

   * O container `db` inicializa o banco `oficina_fase1` com base no script `scripts/create_db_oficina.sql`.
   * O container `api` executa a aplicação FastAPI (porta **8000**).

3. **Acesse a API**

   * Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   * Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

4. **Parar os containers**

   ```bash
   docker-compose down
   ```

---

## Deploy em Kubernetes (EKS)

O deploy é totalmente automatizado via GitHub Actions.

### Pipeline (arquivo `.github/workflows/ci-cd.yml`)

1. **Build e Push da Imagem** → Docker Hub (`lamequesao/oficina-api`)
2. **Criação dos Secrets** no cluster:

   ```bash
   kubectl create secret generic app-secrets \
     --from-literal=USER_DB=${{ secrets.DB_USERNAME }} \
     --from-literal=PASSWORD_DB=${{ secrets.DB_PASSWORD }} \
     --from-literal=SECRET_KEY=${{ secrets.SECRET_KEY }} \
     --dry-run=client -o yaml | kubectl apply -f -
   ```
3. **Aplicação dos manifestos K8s**

   ```bash
   kubectl apply -f k8s/configmap.yaml
   kubectl apply -f k8s/deployment-api.yaml
   kubectl apply -f k8s/service-api.yaml
   kubectl apply -f k8s/hpa.yaml
   ```

### Estrutura Kubernetes

```
k8s/
├── configmap.yaml        # Variáveis de ambiente não sensíveis
├── deployment-api.yaml   # Deployment da aplicação FastAPI
├── hpa.yaml              # Autoescalonador Horizontal
├── service-api.yaml      # Serviço para expor a API
└── secrets.yaml          # (Opcional) Segredos em Base64
```

### Acesso

Após o deploy:

```bash
kubectl get svc
```

Copie o `EXTERNAL-IP` do serviço `fastapi-service` e acesse:

```
http://<EXTERNAL-IP>:8000/docs
```

---

## Provisionamento da Infraestrutura (Terraform)

O provisionamento é feito na pasta `infra/`, contendo os módulos de:

* **VPC**
* **Subnets**
* **RDS (MySQL)**
* **EKS (Cluster Kubernetes)**

### Passos

1. Configure suas credenciais AWS:

   ```bash
   aws configure
   ```
2. Acesse a pasta de infraestrutura:

   ```bash
   cd infra
   ```
3. Inicialize o Terraform:

   ```bash
   terraform init
   ```
4. Planeje e aplique:

   ```bash
   terraform plan
   terraform apply -auto-approve
   ```
5. Ao final, o Terraform exibirá:

   * Endpoint do banco (RDS)
   * Nome do cluster EKS
   * Configurações de acesso (`aws eks update-kubeconfig`)

---

## Testes Automatizados

### Estratégia

* Todos os testes estão localizados em `tests/`.
* São executados automaticamente no pipeline.
* O ambiente de testes usa **MySQL em container** para isolar o banco da produção.

### Execução Local

1. Suba um container MySQL para testes:

```bash
pytest .
```

### Execução no CI/CD

Definição no workflow:

```yaml
- name: Run tests
  env:
    DATABASE_URL: mysql+pymysql://root:root@127.0.0.1:3306/oficina_test
  run: pytest -v
```

---

## Variáveis de Ambiente

| Variável      | Descrição              | Exemplo                    |
| ------------- | ---------------------- | -------------------------- |
| `USER_DB`     | Usuário do banco       | `lameque`                  |
| `PASSWORD_DB` | Senha do banco         | `lameque123`               |
| `HOST_DB`     | Host (ou endpoint RDS) | `db` / `rds.amazonaws.com` |
| `PORT_DB`     | Porta do banco         | `3306`                     |
| `DATABASE`    | Nome do schema         | `oficina_fase1`            |
| `SECRET_KEY`  | Chave JWT              | `fc05c7...f4dc8ff`         |
| `ALGORITHM`   | Algoritmo JWT          | `HS256`                    |

> 💡 Em produção, essas variáveis são gerenciadas via `Secret` no Kubernetes e `Secrets` no GitHub.

---

## Estrutura do Projeto (Resumo)

```
.
├── app/                    # Código-fonte principal (Clean Architecture)
├── tests/                  # Testes unitários e de integração
├── k8s/                    # Manifests Kubernetes
├── infra/                  # Terraform (Infraestrutura AWS)
├── scripts/                # Scripts SQL
├── .github/workflows/      # Pipelines CI/CD
├── Dockerfile
├── docker-compose.yml
└── README.md
```

