# Vigil Summit AI Agent

Sistema inteligente de automação de relacionamento e qualificação de leads para o evento **Vigil Summit**, utilizando Inteligência Artificial para enriquecer dados, personalizar comunicações e aumentar a conversão em reuniões comerciais.

---

# Sumário

- [Arquitetura da Solução](#arquitetura-da-solução)
- [Stack Tecnológico](#stack-tecnológico)
- [Réguas de Comunicação](#réguas-de-comunicação)
- [Estratégia de Dados e Personalização](#estratégia-de-dados-e-personalização)
- [Decisões Estratégicas](#decisões-estratégicas)
- [Plano de Execução](#plano-de-execução-primeiros-5-dias)
- [Escalabilidade](#cenário-de-escala)

---

# Arquitetura da Solução

## Visão Geral

A solução foi projetada para automatizar todo o funil de conversão do Vigil Summit, desde a captação do lead até o agendamento da reunião comercial.

A arquitetura utiliza serviços especializados, persistência em banco relacional, APIs REST desenvolvidas em FastAPI e integração com modelos de linguagem (LLMs) para enriquecimento de dados e personalização de comunicações.

### Fluxo de Negócio

```text
Lead
  ↓
Enriquecimento
  ↓
Qualificação
  ↓
Pré-Evento
  ↓
Pós-Evento
  ↓
Reunião Comercial
```

---

## Componentes

### Entrada de Dados

- Endpoint REST para cadastro de leads
- Integração futura com:
  - Landing Pages
  - Formulários Web
  - LinkedIn Ads
  - CRM

### Camada de Processamento

#### Enrichment Service

Responsável pelo enriquecimento dos dados dos leads.

Exemplos:

- Identificação do setor
- Senioridade
- Porte da empresa
- Perfil profissional

#### Scoring Service

Calcula a relevância comercial do lead.

#### Classification Service

Classifica o lead em categorias como:

- Hot
- Warm
- Cold

#### Action Service

Define as próximas ações automatizadas para cada lead.

#### Pre Event Service

Gerencia as comunicações antes do evento.

#### Post Event Service

Gerencia o relacionamento após o evento.

---

## Camada de Inteligência Artificial

### Modelo Principal

- Claude (Anthropic)

### Modelo Secundário (Fallback)

- OpenAI

Objetivo:

- Personalização de mensagens
- Classificação contextual
- Geração de conteúdo
- Suporte à tomada de decisão

---

## Banco de Dados

### PostgreSQL

Estrutura inicial:

#### leads

Armazena os dados principais dos participantes.

#### enriched_profiles

Armazena informações enriquecidas.

#### interactions

Histórico completo de interações realizadas.

---

## Monitoramento

Dashboard operacional contendo:

- Total de leads
- Leads quentes (Hot)
- Leads mornos (Warm)
- Leads frios (Cold)
- Presenças confirmadas
- Reuniões agendadas
- Taxa de conversão

---

# Stack Tecnológico

## FastAPI

Motivos da escolha:

- Alta performance
- Documentação automática via Swagger/OpenAPI
- Facilidade para APIs orientadas a agentes
- Excelente integração com IA

---

## PostgreSQL

Motivos da escolha:

- Confiabilidade
- Consistência transacional
- Facilidade de modelagem relacional
- Escalabilidade

---

## SQLAlchemy

ORM utilizado para:

- Abstração da camada de persistência
- Mapeamento objeto-relacional
- Facilidade de manutenção

---

## Docker

Utilizado para:

- Padronização do ambiente
- Reprodutibilidade
- Facilidade de deploy
- Isolamento de dependências

---

## Claude (Anthropic)

Modelo principal escolhido por:

- Excelente capacidade de raciocínio
- Forte desempenho em workflows de agentes
- Melhor alinhamento aos requisitos do desafio

---

## OpenAI

Implementado como fallback para:

- Continuidade operacional
- Resiliência da aplicação
- Redução de indisponibilidade

---

# Réguas de Comunicação

## Pré-Evento

### Objetivos

- Confirmar presença
- Reduzir no-show
- Criar antecipação

### Fluxo

#### Dia 0

Confirmação da inscrição.

#### Dia 3

Envio de conteúdo personalizado.

#### 7 dias antes

Lembrete de participação.

#### 1 dia antes

Confirmação final.

### Exemplo

> Olá Carlos, como CISO do setor financeiro, acreditamos que a palestra sobre priorização de riscos em ambientes regulados será especialmente relevante para você.

---

## Pós-Evento

### Objetivos

- Converter participantes em reuniões comerciais
- Nutrir oportunidades qualificadas

### Fluxo

#### Dia do evento

Mensagem de agradecimento.

#### Dia +1

Follow-up personalizado.

#### Dia +3

Convite para reunião.

#### Dia +7

Última tentativa de contato.

### Exemplo

> Olá Carlos, considerando seu interesse em conformidade e gestão de riscos, gostaríamos de apresentar como a Vigil.AI automatiza a priorização de vulnerabilidades para empresas do setor financeiro.

---

# Estratégia de Dados e Personalização

## Dados Coletados

- Nome
- E-mail
- Telefone
- Empresa
- Cargo

---

## Dados Enriquecidos

- Setor
- Porte da empresa
- Senioridade
- Interesses
- Perfil profissional

---

## Utilização dos Dados

As informações enriquecidas são utilizadas para:

- Lead Scoring
- Classificação automática
- Personalização de mensagens
- Priorização comercial
- Segmentação de campanhas

---

## Conformidade com LGPD

Princípios adotados:

- Minimização de dados
- Finalidade específica
- Armazenamento controlado
- Exclusão sob solicitação
- Uso restrito para comunicações relacionadas ao evento

---

# Decisões Estratégicas

## Decisão 1 — PostgreSQL

### Alternativa Avaliada

MongoDB

### Motivo da Escolha

Necessidade de rastreabilidade e relacionamentos claros entre:

- Leads
- Perfis enriquecidos
- Interações

---

## Decisão 2 — Claude como Modelo Principal

### Alternativa Avaliada

Uso exclusivo da OpenAI

### Motivo da Escolha

Maior aderência aos requisitos do desafio e excelente desempenho em fluxos baseados em agentes.

---

## Decisão 3 — Persistência Completa do Histórico

### Alternativa Avaliada

Comunicações sem rastreabilidade

### Motivo da Escolha

Permitir:

- Auditoria
- Personalização contínua
- Histórico comercial
- Métricas de engajamento

---

# Plano de Execução (Primeiros 5 Dias)

## Dia 1

### Infraestrutura

- Configuração Docker
- PostgreSQL
- FastAPI
- Estrutura inicial do projeto

---

## Dia 2

### Persistência

- Modelagem de dados
- CRUD de leads
- Persistência em banco

---

## Dia 3

### Inteligência Artificial

- Serviço de enriquecimento
- Integração com Claude
- Definição de prompts

---

## Dia 4

### Automação

- Réguas de comunicação
- Dashboard operacional
- Métricas iniciais

---

## Dia 5

### Qualidade

- Testes integrados
- Observabilidade
- Ajustes finais
- Preparação para demonstração

---

# Cenário de Escala

## Objetivo

Suportar múltiplos eventos simultaneamente sem necessidade de reescrever a aplicação.

---

## Novo Modelo

### Event

```sql
id
name
segment
location
```

---

### Relacionamento

Todos os leads passam a possuir:

```sql
event_id
```

---

## Segmentação

Cada evento pode possuir:

- Público-alvo específico
- Réguas próprias
- Prompts personalizados

Exemplos:

- Financeiro
- Saúde
- Governo
- Manufatura
- Tecnologia

---

## Escalabilidade

A arquitetura permanece inalterada.

Somente:

- Dados
- Configurações
- Prompts
- Templates

são parametrizados por evento.

Dessa forma, um único agente pode atender dezenas de eventos simultaneamente sem alterações estruturais na plataforma.

---

# Resultado Esperado

O Vigil Summit AI Agent permite:

✅ Automatizar a qualificação de leads

✅ Personalizar comunicações em escala

✅ Reduzir no-show do evento

✅ Melhorar a conversão para reuniões comerciais

✅ Criar rastreabilidade completa da jornada do lead

✅ Escalar para múltiplos eventos utilizando a mesma arquitetura