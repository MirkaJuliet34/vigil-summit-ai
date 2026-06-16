import { useState } from "react";
import api from "../services/api";

export default function Leads() {

  const [form, setForm] = useState({
    name: "",
    email: "",
    phone: "",
    company: "",
    position: ""
  });

  async function submit(e) {

    e.preventDefault();

    const response = await api.post(
      "/leads/",
      form
    );

    alert(
      `Lead ${response.data.name} criado com sucesso`
    );

    setForm({
      name: "",
      email: "",
      phone: "",
      company: "",
      position: ""
    });
  }

  return (
    <div className="container mt-4 mb-5">

      <div className="card p-4">

        <h2 className="mb-4">
          Novo Lead
        </h2>

        <form onSubmit={submit}>

          <div className="mb-3">

            <input
              className="form-control"
              placeholder="Nome"

              value={form.name}

              onChange={(e) =>
                setForm({
                  ...form,
                  name: e.target.value
                })
              }
            />

          </div>

          <div className="mb-3">

            <input
              className="form-control"
              placeholder="Email"

              value={form.email}

              onChange={(e) =>
                setForm({
                  ...form,
                  email: e.target.value
                })
              }
            />

          </div>

          <div className="mb-3">

            <input
              className="form-control"
              placeholder="Telefone"

              value={form.phone}

              onChange={(e) =>
                setForm({
                  ...form,
                  phone: e.target.value
                })
              }
            />

          </div>

          <div className="mb-3">

            <input
              className="form-control"
              placeholder="Empresa"

              value={form.company}

              onChange={(e) =>
                setForm({
                  ...form,
                  company: e.target.value
                })
              }
            />

          </div>

          <div className="mb-4">

            <input
              className="form-control"
              placeholder="Cargo"

              value={form.position}

              onChange={(e) =>
                setForm({
                  ...form,
                  position: e.target.value
                })
              }
            />

          </div>

          <button
            className="btn btn-primary"
            type="submit"
          >
            Cadastrar Lead
          </button>

        </form>

      </div>

    </div>
  );
}