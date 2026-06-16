# Documentação Técnica — Vigil Summit AI Agent

## 1. Visão Geral da Solução

O Vigil Summit AI Agent foi desenvolvido para automatizar o processo de gestão de leads do evento Vigil Summit.

A solução foi projetada para receber participantes, armazenar suas informações, qualificá-los automaticamente, registrar interações e disponibilizar métricas operacionais através de um dashboard centralizado.

O fluxo principal da aplicação é:

```text
Cadastro de Lead
       ↓
Armazenamento
       ↓
Enriquecimento
       ↓
Scoring
       ↓
Classificação
       ↓
Confirmação
       ↓
Follow-up
       ↓
Agendamento de Reunião
```

---

# 2. Arquitetura da Solução

A aplicação foi dividida em três camadas principais:

## Frontend

Responsável pela interface visual utilizada pelos operadores.

Funções:

* Cadastro de leads
* Visualização de métricas
* Consulta de participantes
* Acompanhamento do funil de vendas
* Monitoramento de classificações

---

## Backend

Responsável pela regra de negócio.

Funções:

* Receber requisições da interface
* Validar dados
* Salvar informações no banco
* Executar regras de qualificação
* Integrar com serviços de IA
* Retornar informações ao frontend

---

## Banco de Dados

Responsável pela persistência dos dados.

Funções:

* Armazenar participantes
* Registrar classificações
* Salvar histórico de interações
* Registrar reuniões agendadas

---

# 3. Desenvolvimento do Banco de Dados

## Escolha da Tecnologia

Foi utilizado:

* PostgreSQL 16

Motivos:

* Alta confiabilidade
* Excelente desempenho
* Compatibilidade com Docker
* Integração simples com FastAPI e SQLAlchemy

---

## Estrutura Principal

Tabela principal:

### leads

Campos:

| Campo         | Tipo      |
| ------------- | --------- |
| id            | UUID      |
| nome          | VARCHAR   |
| email         | VARCHAR   |
| telefone      | VARCHAR   |
| empresa       | VARCHAR   |
| cargo         | VARCHAR   |
| score         | INTEGER   |
| classificacao | VARCHAR   |
| confirmado    | BOOLEAN   |
| criado_em     | TIMESTAMP |

---

## Processo de Criação

### Passo 1

Criação do container PostgreSQL via Docker Compose.

### Passo 2

Configuração das variáveis de ambiente.

### Passo 3

Configuração da conexão SQLAlchemy.

### Passo 4

Criação dos modelos ORM.

### Passo 5

Criação automática das tabelas.

### Passo 6

Testes de persistência e consulta.

---

# 4. Desenvolvimento do Backend

## Tecnologia Utilizada

* Python 3.12
* FastAPI
* SQLAlchemy
* Uvicorn

---

## Estrutura de Pastas

```text
backend/
│
├── app/
│   ├── api/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── prompts/
│   └── database/
```

---

## Desenvolvimento Passo a Passo

### Etapa 1

Criação do projeto FastAPI.

### Etapa 2

Configuração do servidor.

### Etapa 3

Configuração do banco PostgreSQL.

### Etapa 4

Criação dos modelos.

### Etapa 5

Criação dos schemas Pydantic.

### Etapa 6

Criação dos endpoints REST.

Exemplos:

```http
POST /leads
GET /leads
GET /metrics
```

### Etapa 7

Implementação da camada de serviços.

Responsabilidades:

* Scoring
* Classificação
* Enriquecimento
* Integração IA

### Etapa 8

Testes de integração.

---

# 5. Desenvolvimento do Frontend

## Objetivo

Disponibilizar uma interface simples para visualização do pipeline comercial.

---

## Funcionalidades Desenvolvidas

### Dashboard

Indicadores:

* Total Leads
* Hot Leads
* Warm Leads
* Cold Leads
* Confirmados
* Reuniões

---

### Cadastro de Leads

Campos:

* Nome
* Email
* Telefone
* Empresa
* Cargo

---

### Listagem

Visualização dos registros cadastrados.

---

### Responsividade

A interface foi adaptada para:

* Desktop
* Notebook
* Tablet
* Smartphone

---

### Design

Foi utilizada uma proposta visual moderna com:

* Tema escuro
* Contraste elevado
* Cards informativos
* Destaque para indicadores estratégicos

---

# 6. Integração com Inteligência Artificial

## Requisito Original

O desafio técnico previa a utilização da API da Anthropic Claude para realizar o enriquecimento e classificação automática dos leads.

Fluxo esperado:

```text
Lead
 ↓
Anthropic Claude
 ↓
Análise
 ↓
Classificação
 ↓
Retorno
```

---

# 7. Limitação Encontrada

Durante os testes foi identificada uma limitação operacional.

Embora a chave da Anthropic estivesse configurada corretamente, a conta utilizada não possuía créditos ativos suficientes para executar chamadas reais da API.

Como consequência, as requisições retornavam erro de autorização para consumo dos modelos.

Isso impossibilitou a validação prática da integração durante o período do desenvolvimento.

---

# 8. Solução Adotada

Para garantir a entrega funcional do projeto dentro do prazo estabelecido, foi implementado um mecanismo alternativo utilizando OpenAI.

Fluxo implementado:

```text
Lead
 ↓
OpenAI
 ↓
Análise
 ↓
Classificação
 ↓
Retorno
```

Benefícios:

* Permitiu validar toda a arquitetura.
* Demonstrou o funcionamento completo do pipeline.
* Manteve a separação da camada de IA.
* Possibilitou futura substituição pela Anthropic sem alterações significativas na aplicação.

---

# 9. Estratégia de Fallback

A arquitetura foi preparada para suportar múltiplos provedores de IA.

Variável de ambiente:

```env
LLM_PROVIDER=anthropic
```

ou

```env
LLM_PROVIDER=openai
```

Dessa forma, a troca entre provedores pode ser realizada sem necessidade de alterações estruturais no código.

---

# 10. Considerações Finais

A solução entregue atende aos requisitos principais do desafio técnico:

✔ Cadastro de participantes

✔ Persistência em PostgreSQL

✔ API REST com FastAPI

✔ Dashboard operacional

✔ Classificação de leads

✔ Arquitetura preparada para IA

✔ Dockerização completa

✔ Estrutura escalável para futuras evoluções

A substituição temporária da Anthropic pela OpenAI ocorreu exclusivamente por indisponibilidade de créditos para execução dos testes, não representando limitação arquitetural da solução, que permanece compatível com ambos os provedores.
