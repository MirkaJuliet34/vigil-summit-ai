export default function About() {

  return (
    <div className="container mt-4 mb-5">

      <div className="card p-4 mb-4">

        <h1>
          Sobre o Projeto
        </h1>

        <p className="text-secondary">
          Vigil Summit AI Agent
        </p>

        <hr />

        <h4>Objetivo</h4>

        <p>
          Solução desenvolvida para automatizar o ciclo de
          engajamento e conversão de participantes do Vigil Summit,
          desde a captação do lead até o agendamento de reuniões
          comerciais.
        </p>

      </div>

      <div className="card p-4 mb-4">

        <h4>
          Fluxo do Agente
        </h4>

        <ul>
          <li>Captação de Leads</li>
          <li>Enriquecimento de Perfil</li>
          <li>Scoring Automático</li>
          <li>Classificação Hot / Warm / Cold</li>
          <li>Confirmação de Participação</li>
          <li>Follow-up Pós Evento</li>
          <li>Agendamento de Reuniões</li>
        </ul>

      </div>

      <div className="card p-4 mb-4">

        <h4>
          Arquitetura de IA
        </h4>

        <p>
          A solução foi projetada utilizando uma camada de abstração
          para Large Language Models (LLMs), permitindo a troca de
          provedores sem impacto na lógica de negócio da aplicação.
        </p>

        <p>
          A arquitetura suporta integração com Anthropic Claude e
          OpenAI através de configuração de ambiente, mantendo uma
          interface única para os serviços responsáveis pelo
          enriquecimento, personalização e automação das interações.
        </p>

        <p>
          Durante a validação do MVP, as execuções foram realizadas
          utilizando OpenAI. A seleção do provedor é controlada pela
          variável de ambiente <code>LLM_PROVIDER</code>, permitindo
          alternância sem alterações estruturais no sistema.
        </p>

      </div>

      <div className="card p-4 mb-4">

        <h4>
          Tecnologias Utilizadas
        </h4>

        <ul>
          <li>Python 3.12</li>
          <li>FastAPI</li>
          <li>PostgreSQL</li>
          <li>SQLAlchemy</li>
          <li>Docker</li>
          <li>React</li>
          <li>Bootstrap</li>
          <li>OpenAI</li>
          <li>Anthropic Ready</li>
        </ul>

      </div>

      <div className="card p-4">

        <h4>
          Escalabilidade
        </h4>

        <p>
          A arquitetura foi concebida para suportar múltiplos
          eventos simultaneamente através da separação entre
          serviços, persistência relacional e camada de IA
          desacoplada, permitindo evolução futura sem reestruturação
          da solução.
        </p>

      </div>

    </div>
  );
}