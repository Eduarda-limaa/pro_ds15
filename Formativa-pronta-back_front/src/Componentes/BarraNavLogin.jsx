import estilo from "./BarraNavLogin.module.css";
import logo from '../images/logo.png';

export function BarraNavLogin() {
  return (
    <nav className={estilo.conteiner}>
      <div className={estilo.logo}>
        <img src={logo} alt="Logo" className={estilo.logoImg} />
      </div>
    </nav>
  );
}