import { Outlet } from "react-router-dom";
import { Footer } from "./Footer";

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
