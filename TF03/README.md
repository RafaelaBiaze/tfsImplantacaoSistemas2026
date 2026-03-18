# TF03 - Sistema de Blog Multi-Container


## Aluno

- **Nome:** Rafaela Bianor de Azevedo

- **RA:** 6324518

- **Curso:** Análise e Desenvolvimento de Sistemas


## Arquitetura

- **Nginx Proxy:** Load balancer e proxy reverso

- **Frontend:** Interface web (HTML/CSS/JS)

- **Backend:** API REST (Python/Node.js/PHP)

- **Database:** MySQL com persistência


## Como Executar


### Pré-requisitos

- Docker e Docker Compose instalados


### Execução

```bash

# Clone o repositório

git clone https://github.com/RafaelaBiaze/tfsImplantacaoSistemas2026.git

cd TF03


# Subir todos os serviços

docker-compose up -d --build


# Verificar status

docker-compose ps


# Acessar aplicação

# Frontend: http://localhost

# API: http://localhost/api/posts