import estilos from './Footer.module.css';
import logo from '../images/logo.png';
export function Footer() {
  return (
    <footer className={estilos.container}>
      <img src={logo} className={estilos.logo} alt="logo" />
      <p>&copy; 2025 Todos os direitos reservados.</p>
    </footer>
  );
}