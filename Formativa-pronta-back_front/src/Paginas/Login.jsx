import axios from 'axios';
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
import estilos from './Login.module.css';
import { useNavigate } from 'react-router-dom';
import { BarraNavLogin } from '../Componentes/BarraNavLogin'

const schemaLogin = z.object({
  username: z.string()
    .min(1, 'Informe seu usuário')
    .max(25, 'Informe até 25 caracteres'),
  password: z.string()
    .min(1, 'Informe ao menos 1 dígito para senha')
    .max(15, 'Informe no máximo 15 caracteres')
});

export function Login() {
  const navigate = useNavigate();

  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    resolver: zodResolver(schemaLogin)
  });

  async function ObterDados(data) {

    try {
      const response = await axios.post('http://127.0.0.1:8000/token/', {
        username: data.username,
        password: data.password
      });

      const { access, refresh, usuario } = response.data;
    

      localStorage.setItem('access_token', access);
      localStorage.setItem('refresh_token', refresh);
      localStorage.setItem('categoria', usuario.categoria);
      localStorage.setItem('username', usuario.username);
      localStorage.setItem('user_id', usuario.id);


    
      navigate('/Inicial');
    } catch (error) {
      alert("Credenciais inválidas");
    }
  }

  return (
    <>
      <BarraNavLogin />

      <div className={estilos.loginContainer}> 
        <form className={estilos.loginForm} onSubmit={handleSubmit(ObterDados)}>
          <h2 className={estilos.titulo}>Login</h2>

          <label>Nome</label>
          <input
            {...register('username')}
            placeholder='username'
          />
          {errors.username && <p>{errors.username.message}</p>}

          <label>Senha</label>
          <input
            {...register('password')}
            placeholder='senha'
            type='password'
          />
          {errors.password && <p>{errors.password.message}</p>}

          <div className={estilos.BotaoContainer}>
            <button className={estilos.botao} type='submit'>Entrar</button>
          </div>
        </form>
      </div>
    </>
  );
}
