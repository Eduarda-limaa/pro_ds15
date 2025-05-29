import { BarraNavegacao } from "../Componentes/BarraNavegacao";
import { Outlet } from 'react-router-dom';
import { Menu } from "../Componentes/Menu";


export function Inicial(){
    return(
        <>
        <BarraNavegacao/>
        <Outlet />
        <Menu/>
        </>
    )
}