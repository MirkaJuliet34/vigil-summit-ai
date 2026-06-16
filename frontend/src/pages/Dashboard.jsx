import { useEffect, useState } from "react";
import api from "../services/api";

export default function Dashboard() {

  const [metrics, setMetrics] = useState(null);

  useEffect(() => {

    api.get("/dashboard/metrics")
      .then((response) => {
        setMetrics(response.data);
      });

  }, []);

  if (!metrics) {

    return (
      <div className="container mt-5">
        <h3>Carregando dashboard...</h3>
      </div>
    );
  }

  return (
    <div className="container mt-4">

      <div className="card hero-card p-4 mb-4">

        <h1>
          Vigil Summit AI
        </h1>

        <p className="text-secondary mb-0">
          Cybersecurity Event Intelligence Platform
        </p>

      </div>

      <div className="row">

        <div className="col-lg-2 col-md-4 col-sm-6 mb-3">

          <div className="card p-3 h-100">

            <div className="section-title">
              Total Leads
            </div>

            <div className="metric-value text-info">
              {metrics.total_leads}
            </div>

          </div>

        </div>

        <div className="col-lg-2 col-md-4 col-sm-6 mb-3">

          <div className="card p-3 h-100">

            <div className="section-title">
              Hot
            </div>

            <div className="metric-value text-danger">
              {metrics.hot}
            </div>

          </div>

        </div>

        <div className="col-lg-2 col-md-4 col-sm-6 mb-3">

          <div className="card p-3 h-100">

            <div className="section-title">
              Warm
            </div>

            <div className="metric-value text-warning">
              {metrics.warm}
            </div>

          </div>

        </div>

        <div className="col-lg-2 col-md-4 col-sm-6 mb-3">

          <div className="card p-3 h-100">

            <div className="section-title">
              Cold
            </div>

            <div className="metric-value text-success">
              {metrics.cold}
            </div>

          </div>

        </div>

        <div className="col-lg-2 col-md-4 col-sm-6 mb-3">

          <div className="card p-3 h-100">

            <div className="section-title">
              Confirmados
            </div>

            <div className="metric-value text-primary">
              {metrics.confirmed}
            </div>

          </div>

        </div>

        <div className="col-lg-2 col-md-4 col-sm-6 mb-3">

          <div className="card p-3 h-100">

            <div className="section-title">
              Reuniões
            </div>

            <div className="metric-value text-info">
              {metrics.meetings}
            </div>

          </div>

        </div>

      </div>

    </div>
  );
}