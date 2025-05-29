import { useEffect, useState } from "react";
import axios from "axios";
import estilos from "./Professores.module.css";
import { BarraNavegacao } from "../Componentes/BarraNavegacao";

export function Professores() {
  const [professores, setProfessores] = useState([]);
  const [loading, setLoading] = useState(true);

  const [modalAberto, setModalAberto] = useState(false);
  const [modoEditar, setModoEditar] = useState(false);
  const [professorSelecionado, setProfessorSelecionado] = useState(null);

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [categoria, setCategoria] = useState("");
  const [ni, setNi] = useState("");
  const [telefone, setTelefone] = useState("");

  const token = localStorage.getItem("access_token");
  const categoriaUsuario = localStorage.getItem("categoria");
  const userId = localStorage.getItem("user_id");

  useEffect(() => {
    async function buscarProfessores() {
      try {
        if (categoriaUsuario === "G") {
          const res = await axios.get("http://127.0.0.1:8000/professores/", {
            headers: { Authorization: `Bearer ${token}` },
          });
          setProfessores(res.data);
        } else {
          const res = await axios.get(
            `http://127.0.0.1:8000/professores/${userId}`,
            {
              headers: { Authorization: `Bearer ${token}` },
            }
          );
          setProfessores([res.data]);
        }
      } catch (error) {
        console.error(
          "Erro ao buscar professores:",
          error.response?.data || error.message
        );
        alert("Erro ao buscar professores.");
      } finally {
        setLoading(false);
      }
    }

    buscarProfessores();
  }, [token, categoriaUsuario, userId]);

  function abrirModalCriar() {
    setModoEditar(false);
    limparFormulario();
    setModalAberto(true);
  }

  function abrirModalEditar(professor) {
    setModoEditar(true);
    setProfessorSelecionado(professor);
    setUsername(professor.username);
    setCategoria(professor.categoria);
    setNi(professor.ni);
    setTelefone(professor.telefone);
    setPassword("");
    setModalAberto(true);
  }

  function limparFormulario() {
    setUsername("");
    setPassword("");
    setCategoria("");
    setNi("");
    setTelefone("");
    setProfessorSelecionado(null);
  }

  async function salvarProfessor() {
    if (password && password.length < 8) {
      alert("A senha deve ter pelo menos 8 caracteres.");
      return;
    }

    if (!/^\d+$/.test(ni)) {
      alert("O NI deve conter apenas números.");
      return;
    }

    if (username.trim().length < 3) {
      alert("O nome de usuário deve ter pelo menos 3 caracteres.");
      return;
    }

    try {
      const dados = {
        username,
        categoria,
        ni,
        telefone,
      };

      if (!modoEditar || password) {
        dados.password = password;
      }

      if (modoEditar && professorSelecionado) {
        await axios.put(
          `http://127.0.0.1:8000/professores/${professorSelecionado.id}`,
          dados,
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );
        setProfessores((old) =>
          old.map((p) =>
            p.id === professorSelecionado.id ? { ...p, ...dados } : p
          )
        );
      } else {
        const res = await axios.post(
          "http://127.0.0.1:8000/professores/",
          dados,
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );
        setProfessores((old) => [...old, res.data]);
      }

      setModalAberto(false);
      limparFormulario();
    } catch (error) {
      console.error(
        "Erro ao salvar professor:",
        error.response?.data || error.message
      );
      const mensagens = error.response?.data;
      if (mensagens && typeof mensagens === "object") {
        const erros = Object.values(mensagens).flat().join("\n");
        alert("Erro ao salvar professor:\n" + erros);
      } else {
        alert("Erro ao salvar professor.");
      }
    }
  }

  async function deletarProfessor(id) {
    if (!window.confirm("Tem certeza que deseja excluir este professor?"))
      return;

    try {
      await axios.delete(`http://127.0.0.1:8000/professores/${id}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setProfessores((old) => old.filter((p) => p.id !== id));
    } catch (error) {
      console.error(
        "Erro ao deletar professor:",
        error.response?.data || error.message
      );
      alert("Erro ao deletar professor.");
    }
  }

  if (loading) return <p>Carregando...</p>;

  return (
    <>
      <BarraNavegacao />
      <div className={estilos.container}>
        <h2 className={estilos.titulo}>
          {categoriaUsuario === "G"
            ? "Lista de Professores"
            : "Informações Pessoais"}
        </h2>

        {categoriaUsuario === "G" && (
          <button className={estilos.botaoCriar} onClick={abrirModalCriar}>
            <span className="material-symbols-outlined">add</span> Novo Professor
          </button>
        )}

        {professores.length > 0 ? (
          <table className={estilos.tabela}>
            <thead>
              <tr>
                <th>Nome</th>
                <th>Categoria</th>
                <th>NI</th>
                <th>Telefone</th>
                {categoriaUsuario === "G" && <th>Ações</th>}
              </tr>
            </thead>
            <tbody>
              {professores.map((p) => (
                <tr key={p.id}>
                  <td>{p.username}</td>
                  <td>{p.categoria}</td>
                  <td>{p.ni}</td>
                  <td>{p.telefone}</td>
                  {categoriaUsuario === "G" && (
                    <td>
                      <button
                        title="Editar"
                        className={estilos.botaoAcao}
                        onClick={() => abrirModalEditar(p)}
                      >
                        <span className="material-symbols-outlined">edit</span>
                      </button>
                      <button
                        title="Excluir"
                        className={estilos.botaoAcao}
                        onClick={() => deletarProfessor(p.id)}
                      >
                        <span className="material-symbols-outlined">delete</span>
                      </button>
                    </td>
                  )}
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p>Nenhum professor encontrado.</p>
        )}
      </div>

      {modalAberto && (
        <div className={estilos.modalOverlay}>
          <div className={estilos.modal}>
            <h3>{modoEditar ? "Editar Professor" : "Novo Professor"}</h3>

            <label>Nome de Usuário</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />

            <label>Senha</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />

            <label>Categoria</label>
            <select
              className={estilos.Selecao}
              value={categoria}
              onChange={(e) => setCategoria(e.target.value)}
            >
              <option value="" disabled>Selecione</option>
              <option value="P">Professor</option>
            </select>

            <label>NI</label>
            <input
              type="text"
              value={ni}
              onChange={(e) => setNi(e.target.value)}
            />

            <label>Telefone</label>
            <input
              type="text"
              value={telefone}
              onChange={(e) => setTelefone(e.target.value)}
              maxLength={10}
            />

            <div className={estilos.modalBotoes}>
              <button className={estilos.botaoSalvar} onClick={salvarProfessor}>
                Salvar
              </button>
              <button
                className={estilos.botaoCancelar}
                onClick={() => {
                  limparFormulario();
                  setModalAberto(false);
                }}
              >
                Cancelar
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
