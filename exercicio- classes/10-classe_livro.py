class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.emprestado = False

    def emprestar_livro (self):
        if not self.emprestado:
            self.emprestado = True
            print(f"O livro {self.titulo} foi emprestado")
        else:
           print("O livro {self.titulo} já está emprestado")
           

    def delvolver_livro(self):
        if self.emprestado:
            self.emprestado = False
            print(f"Livro {self.titulo} foi devolvido")
        else:
            print(f"O livro {self.titulo} não foi emprestado")

    def verificar_livro(self):
        if self.emprestado:
            print(f"O livro {self.titulo} não está disponível")
        else:
            print(f"O livro {self.titulo} está disponível")


livro = Livro('Hary Potter', 'Eliana', 148)
livro.emprestar_livro()
livro.delvolver_livro()
livro.verificar_livro()
