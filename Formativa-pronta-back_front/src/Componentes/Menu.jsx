import { Link } from "react-router-dom";
import estilo from "./Menu.module.css";

export function Menu() {
  if (localStorage.getItem('categoria') == 'G'){
    return (
      <div className={estilo.container}>
        <h2 className={estilo.title}>Acesse as Funcionalidades</h2>
        <div className={estilo.buttonGrid}>
          <Link to="/professores" className={estilo.button}>
            <span className={`material-symbols-outlined ${estilo.icon}`}>book</span>
            Professores
          </Link>

          <Link to="/gestores" className={estilo.button}>
            <span className={`material-symbols-outlined ${estilo.icon}`}>badge</span>
            Gestores
          </Link>

          <Link to="/disciplina" className={estilo.button}>
            <span className={`material-symbols-outlined ${estilo.icon}`}>menu_book</span>
            Disciplina
          </Link>

          <Link to="/ambiente" className={estilo.button}>
            <span className={`material-symbols-outlined ${estilo.icon}`}>home_work</span>
            Ambiente
          </Link>
        </div>
      </div>
    );
  } else  if (localStorage.getItem('categoria') == 'P'){
    return (
      <div className={estilo.container}>
        <h2 className={estilo.title}>Acesse as Funcionalidades</h2>
        <div className={estilo.buttonGrid}>
          <Link to="/professores" className={estilo.button}>
            <span className={`material-symbols-outlined ${estilo.icon}`}>book</span>
            Professores
          </Link>

          <Link to="/disciplina" className={estilo.button}>
            <span className={`material-symbols-outlined ${estilo.icon}`}>menu_book</span>
            Disciplina
          </Link>

          <Link to="/ambiente" className={estilo.button}>
            <span className={`material-symbols-outlined ${estilo.icon}`}>home_work</span>
            Ambiente
          </Link>
        </div>
      </div>
    );
  }
}
