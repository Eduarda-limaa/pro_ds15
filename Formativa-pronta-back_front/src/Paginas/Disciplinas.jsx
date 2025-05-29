import { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import estilos from "./Professores.module.css";
import { BarraNavegacao } from "../Componentes/BarraNavegacao";

export function Disciplinas() {
  const { id } = useParams();
  const [disciplinas, setDisciplinas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [modalAberto, setModalAberto] = useState(false);
  const [modoEditar, setModoEditar] = useState(false);
  const [disciplinaSelecionada, setDisciplinaSelecionada] = useState(null);

  const [nomeDisciplina, setNomeDisciplina] = useState("");
  const [cursoDisciplina, setCursoDisciplina] = useState("");
  const [cargaHorariaDisciplina, setCargaHorariaDisciplina] = useState("");
  const [descricaoDisciplina, setDescricaoDisciplina] = useState("");
  const [professorResponsavelId, setProfessorResponsavelId] = useState("");

  const [professoresDisponiveis, setProfessoresDisponiveis] = useState([]);

  const token = localStorage.getItem("access_token");
  const categoria = localStorage.getItem("categoria");

  useEffect(() => {
    async function buscarDados() {
      try {
        let url =
          categoria === "P"
            ? "http://127.0.0.1:8000/professorDisciplinas/"
            : "http://127.0.0.1:8000/disciplina/";

        const res = await axios.get(url, {
          params: { professor_responsavel: id },
          headers: { Authorization: `Bearer ${token}` },
        });

        setDisciplinas(res.data);
      } catch (error) {
        console.error(
          "Erro ao carregar dados:",
          error.response?.data || error.message
        );
        alert("Erro ao carregar dados.");
      } finally {
        setLoading(false);
      }
    }

    if (categoria) buscarDados();
  }, [id, categoria, token]);

  // buscar professores disponiveis
  useEffect(() => {
    async function buscarProfessores() {
      try {
        const res = await axios.get("http://127.0.0.1:8000/professores/", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setProfessoresDisponiveis(res.data);
      } catch (error) {
        console.error(
          "Erro ao buscar professores:",
          error.response?.data || error.message
        );
      }
    }

    if (categoria === "G") buscarProfessores();
  }, [token, categoria]);

  function abrirModalCriar() {
    setModoEditar(false);
    limparFormulario();
    setModalAberto(true);
  }

  function abrirModalEditar(disciplina) {
    setModoEditar(true);
    setDisciplinaSelecionada(disciplina);
    setNomeDisciplina(disciplina.nome);
    setCursoDisciplina(disciplina.curso);
    setCargaHorariaDisciplina(disciplina.carga_horaria);
    setDescricaoDisciplina(disciplina.descricao);
    setProfessorResponsavelId(disciplina.professor_responsavel);
    setModalAberto(true);
  }

  function limparFormulario() {
    setNomeDisciplina("");
    setCursoDisciplina("");
    setCargaHorariaDisciplina("");
    setDescricaoDisciplina("");
    setProfessorResponsavelId("");
    setDisciplinaSelecionada(null);
  }

  async function salvarDisciplina() {
    try {
      const dados = {
        nome: nomeDisciplina,
        curso: cursoDisciplina,
        carga_horaria: Number(cargaHorariaDisciplina),
        descricao: descricaoDisciplina,
        professor_responsavel: Number(professorResponsavelId),
      };

      if (modoEditar && disciplinaSelecionada) {
        await axios.put(
          `http://127.0.0.1:8000/disciplina/${disciplinaSelecionada.id}/`,
          dados,
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );
        setDisciplinas((old) =>
          old.map((d) =>
            d.id === disciplinaSelecionada.id ? { ...d, ...dados } : d
          )
        );
      } else {
        const res = await axios.post(
          "http://127.0.0.1:8000/disciplina/",
          dados,
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );
        setDisciplinas((old) => [...old, res.data]);
      }

      setModalAberto(false);
      limparFormulario();
    } catch (error) {
      const erroData = error.response?.data;
      let mensagem = "Erro ao salvar.";
    
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

  async function deletarDisciplina(idDisciplina) {
    if (!window.confirm("Tem certeza que deseja excluir esta disciplina?"))
      return;

    try {
      await axios.delete(`http://127.0.0.1:8000/disciplina/${idDisciplina}/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setDisciplinas((old) => old.filter((d) => d.id !== idDisciplina));
    } catch (error) {
      console.error(
        "Erro ao deletar disciplina:",
        error.response?.data || error.message
      );
      alert("Erro ao deletar disciplina.");
    }
  }

  if (loading) return <p>Carregando...</p>;

  return (
    <>
      <BarraNavegacao />
      <div className={estilos.container}>
        <h2 className={estilos.titulo}>
          {categoria === "G"
            ? "Controle de Disciplinas"
            : "Disciplinas Atribuídas"}
        </h2>

        {categoria === "G" && (
          <button className={estilos.botaoCriar} onClick={abrirModalCriar}>
            <span className="material-symbols-outlined">add</span> Nova
            Disciplina
          </button>
        )}

        {disciplinas.length > 0 ? (
          <table className={estilos.tabela}>
            <thead>
              <tr>
                <th>Nome</th>
                <th>Curso</th>
                <th>Carga Horária</th>
                <th>Descrição</th>
                {categoria === "G" && <th>Professor Responsável</th>}
                {categoria === "G" && <th>Ações</th>}
              </tr>
            </thead>
            <tbody>
              {disciplinas.map((d) => (
                <tr key={d.id}>
                  <td>{d.nome}</td>
                  <td>{d.curso}</td>
                  <td>{d.carga_horaria}h</td>
                  <td>{d.descricao}</td>
                  {categoria === "G" && (
                    <>
                      <td>
                        {
                          professoresDisponiveis.find(
                            (prof) => prof.id === d.professor_responsavel
                          )?.username || "Não definido"
                        }
                      </td>
                      <td>
                        <button
                          title="Editar"
                          className={estilos.botaoAcao}
                          onClick={() => abrirModalEditar(d)}
                        >
                          <span className="material-symbols-outlined">edit</span>
                        </button>
                        <button
                          title="Excluir"
                          className={estilos.botaoAcao}
                          onClick={() => deletarDisciplina(d.id)}
                        >
                          <span className="material-symbols-outlined">delete</span>
                        </button>
                      </td>
                    </>
                  )}
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p>Sem disciplinas cadastradas</p>
        )}
      </div>

      {modalAberto && (
        <div className={estilos.modalOverlay}>
          <div className={estilos.modal}>
            <h3>{modoEditar ? "Editar Disciplina" : "Nova Disciplina"}</h3>
            <label>Nome</label>
            <input
              type="text"
              value={nomeDisciplina}
              onChange={(e) => setNomeDisciplina(e.target.value)}
            />

            <label>Curso</label>
            <input
              type="text"
              value={cursoDisciplina}
              onChange={(e) => setCursoDisciplina(e.target.value)}
            />

            <label>Carga Horária</label>
            <input
              type="number"
              value={cargaHorariaDisciplina}
              onChange={(e) => setCargaHorariaDisciplina(e.target.value)}
            />

            <label>Descrição</label>
            <textarea
              rows={3}
              value={descricaoDisciplina}
              onChange={(e) => setDescricaoDisciplina(e.target.value)}
            />

            <label>Professor Responsável</label>
            <select className={estilos.Selecao}
              value={professorResponsavelId}
              onChange={(e) => setProfessorResponsavelId(e.target.value)}
            >
              <option value="">Selecione</option>
              {professoresDisponiveis.map((prof) => (
                <option key={prof.id} value={prof.id}>
                  {prof.username}
                </option>
              ))}
            </select>

            <div className={estilos.modalBotoes}>
              <button className={estilos.botaoSalvar} onClick={salvarDisciplina}>
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
