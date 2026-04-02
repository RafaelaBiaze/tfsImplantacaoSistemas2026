# TF05 - Sistema de Monitoramento e Automação

Este documento detalha a arquitetura, os componentes e os processos de automação do projeto **TechNova Monitoring**, focado em alta disponibilidade e monitoramento inteligente.

## Aluno
- **Nome:** Rafaela Bianor de Azevedo
- **RA:** 6324518
- **Curso:** Análise e Desenvolvimento de Sistemas

---

## Estrutura do Projeto

A organização das pastas segue as melhores práticas de **DevOps**, separando responsabilidades entre infraestrutura, aplicação e monitoramento.

```text
TF05/
├── api/                # Backend em Python (Flask) para coleta de métricas
├── config/             # Configurações YAML (Healthchecks, Alertas)
├── dashboard/          # Interface Web (HTML/JS) de monitoramento
├── database/           # Scripts de inicialização do MySQL
├── docs/               # Documentação técnica detalhada
├── scripts/            # Automação de Build, Deploy e Manutenção
└── docker-compose.yml  # Orquestração de containers
```

---

## Papel dos Componentes

1. **Docker Compose** (docker-compose.yml)
O mapa da infraestrutura. Ele define como os containers se conectam, quais portas estão abertas e como os dados são persistidos. É a ferramenta que executa o plano definido.

2. **Scripts de Automação** (/scripts)
São os procedimentos operacionais. Eles envolvem o Docker Compose com camadas de segurança (backup), validação e manutenção que o Docker sozinho não realiza.

---

## Comparativo: Docker Compose vs. Automação

A tabela abaixo explica por que utilizamos scripts em vez de apenas comandos puros do Docker em ambientes profissionais.

| Ação | Docker Compose | Scripts Automação |
| :--- | :---: | ---: |
| **Build** |`docker-compose` build cria a imagem de forma simples. | O `build.sh` limpa o cache, valida arquivos e prepara o ambiente antes de construir. |
| **Segurança** | Substitui os arquivos atuais imediatamente no deploy. | O `deploy.sh` realiza um backup automático das configurações antes de qualquer alteração. |
| **Disponibilidade** | Pode haver instabilidade durante o reinício do serviço. | Scripts podem implementar o Zero Downtime, garantindo que o serviço nunca fique fora do ar. |
| **Recuperação** | Exige correção manual caso o deploy falhe. | O `rollback.sh` restaura a versão anterior funcional com um único comando. |
| **Manutenção** | Acúmulo de imagens e logs antigos no disco. | O `cleanup.sh` automatiza a limpeza de recursos órfãos, preservando o espaço no servidor. |

---

## Fluxo de Operação

Para operar o sistema de forma segura, siga a ordem dos scripts abaixo:

### Construção:

```Bash
./scripts/build.sh
```
Garante que as imagens estão atualizadas e sem erros.

### Implantação:

```Bash
./scripts/deploy.sh
```
Faz o backup das configurações e sobe o sistema.

### Monitoramento:

```Bash
./scripts/health-monitor.sh
```
Verifica o status de saúde dos serviços via terminal.

### Limpeza:

```Bash
./scripts/cleanup.sh
```
Remove resíduos e libera espaço em disco.

---

## Monitoramento Inteligente
O sistema está configurado para realizar três tipos de validações essenciais:

1. **HTTP**: Verifica se as páginas web e APIs estão respondendo (Status 200).

2. **TCP**: Garante que as portas de comunicação (como a do Banco de Dados) estão abertas.

3. **Database**: Executa comandos simples no SQL para confirmar que o banco está processando dados.

4. **Pro-Tip**: Sempre verifique o Dashboard em http://localhost:3000 após um deploy para confirmar visualmente se todos os indicadores estão verdes.