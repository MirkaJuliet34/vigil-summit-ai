import { useState } from "react";

import Dashboard from "./pages/Dashboard";
import Leads from "./pages/Leads";
import About from "./pages/About";
import AIProvider from "./pages/AIProvider";

function App() {

  const [page, setPage] = useState("dashboard");

  return (
    <div className="app-layout">

      <aside className="sidebar">

        <div className="sidebar-header">

          <h3>
            ⚡ Vigil Summit AI
          </h3>

          <p>
            Cybersecurity Platform
          </p>

        </div>

        <div className="sidebar-menu">

          <button
            className={`menu-btn ${
              page === "dashboard"
                ? "active"
                : ""
            }`}
            onClick={() =>
              setPage("dashboard")
            }
          >
            📊 Dashboard
          </button>

          <button
            className={`menu-btn ${
              page === "leads"
                ? "active"
                : ""
            }`}
            onClick={() =>
              setPage("leads")
            }
          >
            👥 Leads
          </button>

          <button
            className={`menu-btn ${
              page === "about"
                ? "active"
                : ""
            }`}
            onClick={() =>
              setPage("about")
            }
          >
            📄 Sobre o Projeto
          </button>

          <button
            className={`menu-btn ${
              page === "provider"
                ? "active"
                : ""
            }`}
            onClick={() =>
              setPage("provider")
            }
          >
            🤖 AI Provider
          </button>

        </div>

      </aside>

      <main className="content">

        {page === "dashboard" && (
          <Dashboard />
        )}

        {page === "leads" && (
          <Leads />
        )}

        {page === "about" && (
          <About />
        )}

        {page === "provider" && (
          <AIProvider />
        )}

      </main>

    </div>
  );
}

export default App;