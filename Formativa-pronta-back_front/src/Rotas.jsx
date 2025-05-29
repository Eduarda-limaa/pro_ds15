import { Routes, Route, Navigate } from 'react-router-dom';
import { Inicial } from './Paginas/Inicial';
import { Login } from './Paginas/Login';
import { Professores } from './Paginas/Professores';
import { Reservas } from './Paginas/Reservas';
import { Disciplinas } from './Paginas/Disciplinas';
import { Layout } from './Componentes/Layout';
import { Gestores } from './Paginas/Gestores';

export function Rotas() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" />} />
      <Route path="/login" element={<Login />} />
      <Route element={<Layout />}>
        <Route path="/inicial" element={<Inicial />} />
        <Route path="/professores" element={<Professores />} />
        <Route path="/ambiente" element={<Reservas />} />
        <Route path="/disciplina" element={<Disciplinas />} />
        <Route path="/gestores" element={<Gestores />} />
      </Route>
    </Routes>
  );
}
