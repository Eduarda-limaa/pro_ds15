import { Outlet } from "react-router-dom";
import { Footer } from "./Footer";

// Componente que organiza outros componentes para cada um ficar na sua devida possição
export function Layout() {
  return (
    <div className="layout">
      <main className="main-content">
        <Outlet />
      </main>
      <Footer />
    </div>
  );
}
