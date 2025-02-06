class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome= nome
        self.salario= salario
        self.cargo= cargo


    def calculo_salario(self):
        desconto= self.salario * 0.1
        beneficio= self.salario * 0.1
        conta= self.salario - desconto - beneficio
        print(conta)


funcionarios= Funcionario("Angelo", 15000, "Gerente de projetos")
funcionarios.calculo_salario()