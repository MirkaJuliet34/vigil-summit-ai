# Vigil Summit AI Agent

## Arquitetura da Solução

---

# Visão Geral

A solução **Vigil Summit AI Agent** foi desenvolvida para automatizar o ciclo completo de conversão de participantes do evento Vigil Summit, desde a geração do lead até o agendamento de reuniões comerciais.

O sistema combina APIs REST, persistência relacional, serviços especializados e modelos de linguagem (LLMs) para personalização, enriquecimento de dados e tomada de decisão automatizada.

---

# Arquitetura Lógica

```text
+-------------------+
|   Lead Capture    |
+-------------------+
          |
          v
+-------------------+
|    FastAPI API    |
+-------------------+
          |
          v
+-------------------+
|    Agent Layer    |
+-------------------+
          |
          +------------------------------------------------+
          |                |               |               |
          v                v               v               v
   Enrichment        Scoring Engine   Classification   Actions Engine

          |
          v

+-------------------+
|    PostgreSQL     |
+-------------------+
          |
          +----------------------------+
          |                            |
          v                            v
 Enriched Profiles              Interactions

          |
          v

+-------------------+
| Communication     |
| Layer             |
+-------------------+
          |
          +-------------------+
          |                   |
          v                   v
      Pre-Event          Post-Event

          |
          v

+-------------------+
|    Dashboard      |
+-------------------+
```

---

# Componentes

## Lead Capture

Responsável pela entrada dos leads no sistema.

### Implementação Atual

- Endpoint REST

### Evoluções Futuras

- Landing Pages
- LinkedIn Lead Forms
- Chatbots
- Webhooks
- Integrações com CRMs

---

## Agent Layer

Camada central responsável pela tomada de decisão automatizada.

### Serviços

- EnrichmentService
- ScoringService
- ClassificationService
- ActionService
- PreEventService
- PostEventService

---

## Enrichment Engine

### Objetivo

Transformar dados básicos em contexto de negócio para aumentar a qualidade da análise.

### Entrada

- Nome
- Cargo
- Empresa

### Saída

- Setor de atuação
- Senioridade
- Porte da empresa
- Interesses potenciais
- Perfil profissional

---

## Scoring Engine

Responsável por calcular a prioridade comercial de cada lead.

### Exemplo de Regras

| Critério | Pontuação |
|-----------|------------|
| CISO | +40 |
| CTO | +35 |
| Área Financeira | +20 |
| Healthcare | +20 |
| Empresa de Grande Porte | +20 |

### Resultado

Score final utilizado para classificação automática.

---

## Classification Engine

Classifica automaticamente os leads com base na pontuação obtida.

| Classificação | Score |
|--------------|--------|
| Hot | ≥ 70 |
| Warm | 40 – 69 |
| Cold | < 40 |

---

## Action Engine

Determina automaticamente a próxima ação para cada lead.

### Exemplos

| Classificação | Ação |
|--------------|------|
| Hot | Invite VIP |
| Warm | Send Confirmation |
| Cold | Send Nurturing |

---

## Communication Layer

Responsável pela execução das interações com os participantes.

### Pré-Evento

- Confirmação de participação
- Engajamento
- Lembretes automáticos

### Pós-Evento

- Follow-up
- Convite comercial
- Agendamento de reuniões
- Nutrição de leads

---

## LLM Layer

Camada de Inteligência Artificial responsável pela personalização e geração de conteúdo.

### Modelo Principal

- Anthropic Claude

### Fallback

- OpenAI

### Funções

- Personalização de mensagens
- Geração de conteúdo
- Enriquecimento contextual
- Priorização de oportunidades
- Suporte à tomada de decisão

---

## Banco de Dados

### Leads

Armazena os participantes cadastrados.

**Principais informações:**

- Dados pessoais
- Dados corporativos
- Status atual

### Enriched Profiles

Armazena informações geradas pelo mecanismo de enriquecimento.

**Exemplos:**

- Senioridade
- Setor
- Porte da empresa
- Perfil profissional

### Interactions

Armazena o histórico completo de comunicação.

**Exemplos:**

- E-mails enviados
- Confirmações
- Follow-ups
- Reuniões agendadas

---

# Fluxo de Dados

1. O lead entra na plataforma.
2. Os dados são persistidos no banco.
3. O perfil é enriquecido.
4. O score comercial é calculado.
5. O lead é classificado.
6. A próxima ação é definida.
7. A interação é registrada.
8. As comunicações são executadas.
9. A reunião comercial é agendada.

---

# Benefícios da Arquitetura

## Escalabilidade

Separação clara de responsabilidades permitindo crescimento horizontal dos serviços.

## Observabilidade

Histórico completo de eventos e interações para monitoramento e auditoria.

## Extensibilidade

Novos canais de comunicação podem ser adicionados sem alterar a lógica central.

## Reutilização

O mesmo agente pode operar simultaneamente em múltiplos eventos e campanhas.

## Conformidade

Estrutura preparada para requisitos de LGPD, governança e auditoria corporativa.

---

# Stack Tecnológica

| Camada | Tecnologia |
|----------|------------|
| Backend API | FastAPI |
| Banco de Dados | PostgreSQL |
| IA Generativa | Claude / OpenAI |
| Dashboard | React |
| Persistência | SQLAlchemy |
| Containerização | Docker |
| Orquestração | Docker Compose |

---

# Roadmap Futuro

- Integração com LinkedIn
- Integração com HubSpot
- Integração com Salesforce
- WhatsApp Business API
- Microsoft Teams
- Calendly
- Enriquecimento via APIs externas
- Motor de recomendação baseado em IA
- Analytics avançado
- Multi-eventos
- Multi-tenant

---

## Resultado Esperado

Transformar participantes do Vigil Summit em oportunidades qualificadas de negócio por meio de um agente autônomo capaz de:

- Enriquecer informações
- Priorizar leads
- Personalizar interações
- Automatizar comunicações
- Agendar reuniões comerciais
- Gerar inteligência de vendas em escala