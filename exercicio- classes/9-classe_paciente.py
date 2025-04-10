class Paciente:
    def __init__(self, nome, idade, historico):
        self.nome = nome
        self.idade = idade
        self.historico = historico

    def adicionar(self):
        self.historico += 1
        print("Consulta adicionada")

    def exibir(self):
        print(f"Foi realizada o total de {self.historico} consultas")
        

paciente = Paciente('Giovana', 19, 4 )
paciente.adicionar()
paciente.adicionar()
paciente.exibir()