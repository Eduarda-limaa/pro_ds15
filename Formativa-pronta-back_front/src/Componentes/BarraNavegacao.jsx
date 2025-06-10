import estilo from "./BarraNavegacao.module.css";
import { Link } from "react-router-dom";
import logo from '../images/logo.png';


export function BarraNavegacao() {
  return (
    <nav className={estilo.conteiner}>
      <div className={estilo.logo}>
        <img src={logo} alt="Logo" className={estilo.logoImg} />
      </div>

      <ul className={estilo.lista}>
        <li>
          <Link to="/inicial" className={estilo.link}>
            <span className="material-symbols-outlined">school</span>
            Escola
          </Link>
        </li>
        <li>
          <Link to="/login" className={estilo.link}>
            <span className="material-symbols-outlined">person</span>
            Login
          </Link>
        </li>
      </ul>
    </nav>
  );
}
