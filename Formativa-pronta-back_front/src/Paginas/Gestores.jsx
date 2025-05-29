import { useEffect, useState } from 'react';
import axios from 'axios';
import estilos from './Professores.module.css';
import { BarraNavegacao } from '../Componentes/BarraNavegacao';

export function Gestores() {
  const [professor, setProfessor] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function buscarDados() {
      try {
        const token = localStorage.getItem('access_token');
        const id = localStorage.getItem('user_id');
        const resposta = await axios.get(`http://127.0.0.1:8000/professores/${id}`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });

        setProfessor(resposta.data);
      } catch (error) {
        console.error('Erro ao buscar dados do Gestor (a):', error);
        alert('Erro ao buscar dados do Gestor (a)');
      } finally {
        setLoading(false);
      }
    }

    buscarDados();
  }, []);

  if (loading) return <p>Carregando dados...</p>;

  return (
    <>
      <BarraNavegacao />
      <div className={estilos.container}>
        <h2 className={estilos.titulo}>Informações Pessoais do Gestor (a) </h2>
        {professor && (
          <table className={estilos.tabela}>
            <tbody>
              <tr>
                <th>Nome de Usuário</th>
                <td>{professor.username}</td>
              </tr>
              <tr>
                <th>Categoria</th>
                <td>{professor.categoria}</td>
              </tr>
              <tr>
                <th>NI</th>
                <td>{professor.ni}</td>
              </tr>
              <tr>
                <th>Telefone</th>
                <td>{professor.telefone}</td>
              </tr>
            </tbody>
          </table>
        )}
      </div>
    </>
  );
}
