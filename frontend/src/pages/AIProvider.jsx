import { useEffect, useState } from "react";
import api from "../services/api";

export default function AIProvider() {

  const [provider, setProvider] = useState("loading");

  useEffect(() => {

    api.get("/ai/provider")
      .then((response) => {

        setProvider(
          response.data.provider
        );

      })
      .catch(() => {

        setProvider("unknown");

      });

  }, []);

  return (

    <div className="container mt-4">

      <div className="card p-4 mb-4">

        <h1>
          🤖 AI Provider
        </h1>

        <p className="text-secondary">
          Multi-LLM Architecture Overview
        </p>

      </div>

      <div className="row">

        <div className="col-md-6 mb-3">

          <div className="card p-4">

            <h5>
              Provider Atual
            </h5>

            <h2 className="text-info">
              {provider}
            </h2>

          </div>

        </div>

        <div className="col-md-6 mb-3">

          <div className="card p-4">

            <h5>
              Multi-LLM
            </h5>

            <h2 className="text-success">
              Enabled
            </h2>

          </div>

        </div>

        <div className="col-md-6 mb-3">

          <div className="card p-4">

            <h5>
              Anthropic Ready
            </h5>

            <h2 className="text-warning">
              Yes
            </h2>

          </div>

        </div>

        <div className="col-md-6 mb-3">

          <div className="card p-4">

            <h5>
              Environment
            </h5>

            <h2 className="text-primary">
              Docker
            </h2>

          </div>

        </div>

      </div>

      <div className="card p-4">

        <h4>
          Arquitetura
        </h4>

        <p>
          A aplicação utiliza uma camada de abstração
          para Large Language Models (LLMs),
          permitindo alternância entre provedores
          sem impacto na lógica de negócio.
        </p>

        <p>
          O provedor ativo é definido através da
          variável de ambiente
          <code> LLM_PROVIDER </code>,
          possibilitando utilização de OpenAI
          ou Anthropic Claude com o mesmo fluxo
          operacional.
        </p>

      </div>

    </div>

  );
}