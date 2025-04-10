# inicia a classe aluno
class Aluno:

    def __init__(self, nome, matricula, notas):
        
        self.nome= nome
        self.matricula= matricula
        self.notas= notas

# calcula a media do aluno
    def calcular_nota(self):
        v = 0
        for i in self.notas:
            v += i
            tamanho = len(self.notas)
            m = v / tamanho
        return m
    
    # verifica a situação do aluno baseado na média
    def situacao_aluno(self):
        media= self.calcular_nota()
        if media >= 5:
           print("Aprovado!")
        else:
           print("Reprovado!")
            
# chama as funções
aluno= Aluno("Veronica", 1234, [10,7, 8])
print(aluno.calcular_nota())
print(aluno.situacao_aluno())



