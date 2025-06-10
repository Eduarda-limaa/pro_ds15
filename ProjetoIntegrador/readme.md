# Passo a Passo para rodar este sistema

Este documento descreve como configurar e executar corretamente o sistema em sua máquina local.

# Clonar o Repositório

Para começar, clone este repositório em seu computador:

1.  Acesse a página do repositório no GitHub.
    
2.  Clique no botão verde **"Code"**.
    
3.  Copie a URL exibida (HTTPS ou SSH).
    
4.  Abra o terminal no local onde deseja salvar o projeto e execute:
	  `git clone <url-projeto>`
	  Substitua `<url-projeto>` pela URL que você copiou.
	  
	 
## Criar e Ativar o Ambiente Virtual

Crie o ambiente virtual com o seguinte comando:
`python -m venv env`

Ative a **Env** no terminal:
 `.\env\Scripts\activate`

## Instale as dependências do projeto

Com o ambiente ativado, instale todas as dependências do projeto:
`pip install -r .\requirements.txt` 

## Aplicar Migrações

Antes de rodar o servidor, é necessário preparar o banco de dados.
**Criar os arquivos de migração:**
`python .\manage.py makemigrations api`

**Aplicar as migrações:**
`python manage.py migrate`


## Criar um Superuser

Para acessar o painel administrativo do Django, crie um superusuário com:
`python manage.py createsuperuser`
Siga as instruções do terminal para definir nome, e-mail e senha.

## Execute o Servidor

Por fim, inicie o servidor de desenvolvimento com:
`python .\manage.py runserver`



