import { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import estilos from "./Professores.module.css";
import { BarraNavegacao } from "../Componentes/BarraNavegacao";

export function Reservas() {
  const { id } = useParams();
  const [reservas, setReservas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [modalAberto, setModalAberto] = useState(false);
  const [modoEditar, setModoEditar] = useState(false);
  const [reservaSelecionada, setReservaSelecionada] = useState(null);
  const [sala, setSala] = useState("");
  const [periodo, setPeriodo] = useState("");
  const [dataInicio, setDataInicio] = useState("");
  const [dataTermino, setDataTermino] = useState("");
  const [professorResponsavel, setProfessorResponsavel] = useState("");
  const [disciplina, setDisciplina] = useState("");
  const [professores, setProfessores] = useState([]);
  const [disciplinas, setDisciplinas] = useState([]);
  const [disciplinasFiltradas, setDisciplinasFiltradas] = useState([]);

  const token = localStorage.getItem("access_token");
  const categoriaUsuario = localStorage.getItem("categoria");
  const userId = localStorage.getItem("user_id");

  useEffect(() => {
    async function buscarReservas() {
      try {
        let res;
        if (categoriaUsuario === "G") {
          res = await axios.get("http://127.0.0.1:8000/reservaAmbiente/", {
            headers: { Authorization: `Bearer ${token}` },
          });
        } else {
          res = await axios.get("http://127.0.0.1:8000/professorReservas/", {
            params: { professor_responsavel: userId },
            headers: { Authorization: `Bearer ${token}` },
          });
        }
        setReservas(res.data);
      } catch (error) {
        console.error("Erro ao carregar reservas:", error.response?.data || error.message);
        alert("Erro ao carregar reservas.");
      } finally {
        setLoading(false);
      }
    }

    async function carregarProfessores() {
      try {
        const res = await axios.get("http://127.0.0.1:8000/professores/", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setProfessores(res.data);
      } catch (error) {
        console.error("Erro ao carregar professores:", error.response?.data || error.message);
      }
    }

    async function carregarDisciplinas() {
      try {
        const res = await axios.get("http://127.0.0.1:8000/disciplina/", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setDisciplinas(res.data);
      } catch (error) {
        console.error("Erro ao carregar disciplinas:", error.response?.data || error.message);
      }
    }

    buscarReservas();
    if (categoriaUsuario === "G") {
      carregarProfessores();
      carregarDisciplinas();
    }
  }, [categoriaUsuario, token, userId]);

  useEffect(() => {
    const filtradas = disciplinas.filter(
      (d) => String(d.professor_responsavel) === String(professorResponsavel)
    );
    setDisciplinasFiltradas(filtradas);
  }, [professorResponsavel, disciplinas]);

  function abrirModalCriar() {
    setModoEditar(false);
    limparFormulario();
    setModalAberto(true);
  }

  function abrirModalEditar(reserva) {
    setModoEditar(true);
    setReservaSelecionada(reserva);
    setSala(reserva.sala);
    setPeriodo(reserva.periodo);
    setDataInicio(reserva.data_inicio);
    setDataTermino(reserva.data_termino);
    setProfessorResponsavel(reserva.professor_responsavel);
    setDisciplina(reserva.disciplina);
    setModalAberto(true);
  }

  function limparFormulario() {
    setSala("");
    setPeriodo("");
    setDataInicio("");
    setDataTermino("");
    setProfessorResponsavel("");
    setDisciplina("");
    setReservaSelecionada(null);
  }

  async function salvarReserva() {
    const isDataValida = new Date(dataInicio) <= new Date(dataTermino);
    if (!isDataValida) {
      alert("A data de início não pode ser posterior à data de término.");
      return;
    }

    if (!sala || !periodo || !dataInicio || !dataTermino || !professorResponsavel || !disciplina) {
      alert("Preencha todos os campos obrigatórios.");
      return;
    }

    try {
      const dados = {
        sala,
        periodo,
        data_inicio: dataInicio,
        data_termino: dataTermino,
        professor_responsavel: professorResponsavel,
        disciplina: disciplina,
      };

      if (modoEditar && reservaSelecionada) {
        await axios.put(
          `http://127.0.0.1:8000/reservaAmbiente/${reservaSelecionada.id}`,
          dados,
          { headers: { Authorization: `Bearer ${token}` } }
        );
        setReservas((old) =>
          old.map((r) => (r.id === reservaSelecionada.id ? { ...r, ...dados } : r))
        );
      } else {
        const res = await axios.post("http://127.0.0.1:8000/reservaAmbiente/", dados, {
          headers: { Authorization: `Bearer ${token}` },
        });
        setReservas((old) => [...old, res.data]);
      }

      setModalAberto(false);
      limparFormulario();
    } catch (error) {
      const erroData = error.response?.data;
      let mensagem = "Erro ao salvar reserva.";

      if (erroData) {
        const primeiroValor = Object.values(erroData)[0];
        if (Array.isArray(primeiroValor)) {
          mensagem = primeiroValor[0];
        } else if (typeof primeiroValor === "string") {
          mensagem = primeiroValor;
        }
      }
      alert(mensagem);
    }
  }

  async function deletarReserva(id) {
    if (!window.confirm("Tem certeza que deseja excluir esta reserva?")) return;

    try {
      await axios.delete(`http://127.0.0.1:8000/reservaAmbiente/${id}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setReservas((old) => old.filter((r) => r.id !== id));
    } catch (error) {
      console.error("Erro ao deletar reserva:", error.response?.data || error.message);
      alert("Erro ao deletar reserva.");
    }
  }

  if (loading) return <p>Carregando...</p>;

  return (
    <>
      <BarraNavegacao />
      <div className={estilos.container}>
        <h2 className={estilos.titulo}>Ambientes Reservados</h2>

        {categoriaUsuario === "G" && (
          <button className={estilos.botaoCriar} onClick={abrirModalCriar}>
            <span className="material-symbols-outlined">add</span> Nova Reserva
          </button>
        )}

        {reservas.length > 0 ? (
          <table className={estilos.tabela}>
            <thead>
              <tr>
                <th>Sala</th>
                <th>Período</th>
                <th>Data Início</th>
                <th>Data Término</th>
                {categoriaUsuario === "G" && <th>Ações</th>}
              </tr>
            </thead>
            <tbody>
              {reservas.map((r) => (
                <tr key={r.id}>
                  <td>{r.sala}</td>
                  <td>{r.periodo}</td>
                  <td>{r.data_inicio}</td>
                  <td>{r.data_termino}</td>
                  {categoriaUsuario === "G" && (
                    <td>
                      <button
                        title="Editar"
                        className={estilos.botaoAcao}
                        onClick={() => abrirModalEditar(r)}
                      >
                        <span className="material-symbols-outlined">edit</span>
                      </button>
                      <button
                        title="Excluir"
                        className={estilos.botaoAcao}
                        onClick={() => deletarReserva(r.id)}
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
          <p>Sem reservas cadastradas</p>
        )}
      </div>

      {modalAberto && categoriaUsuario === "G" && (
        <div className={estilos.modalOverlay}>
          <div className={estilos.modal}>
            <h3>{modoEditar ? "Editar Reserva" : "Nova Reserva"}</h3>

            <label>Sala</label>
            <input
              type="text"
              value={sala}
              onChange={(e) => setSala(e.target.value)}
            />

            <label>Período</label>
            <input
              type="text"
              value={periodo}
              onChange={(e) => setPeriodo(e.target.value)}
            />

            <label>Data Início</label>
            <input
              type="date"
              value={dataInicio}
              onChange={(e) => setDataInicio(e.target.value)}
            />

            <label>Data Término</label>
            <input
              type="date"
              value={dataTermino}
              onChange={(e) => setDataTermino(e.target.value)}
            />

            <label>Professor Responsável</label>
            <select className={estilos.Selecao}
              value={professorResponsavel}
              onChange={(e) => setProfessorResponsavel(e.target.value)}
            >
              <option value="">Selecione um professor</option>
              {professores.map((p) => (
                <option key={p.id} value={p.id}>
                  {p.username}
                </option>
              ))}
            </select>

            <label>Disciplina</label>
            <select className={estilos.Selecao}
              value={disciplina}
              onChange={(e) => setDisciplina(e.target.value)}
            >
              <option value="">Selecione uma disciplina</option>
              {disciplinasFiltradas.map((d) => (
                <option key={d.id} value={d.id}>
                  {d.nome}
                </option>
              ))}
            </select>

            <div className={estilos.modalBotoes}>
              <button className={estilos.botaoSalvar} onClick={salvarReserva}>
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
