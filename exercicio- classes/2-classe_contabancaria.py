# iniciando a classe
class ContaBancaria:

    def __init__(self, num_conta, nome, saldo):

        self.num_conta= num_conta
        self.nome= nome
        self.saldo= saldo 

# calculando o deposito
    def deposito(self, valor):
        
        self.saldo += valor
        return self.saldo
    
# calculando o saque
    def saque(self, valor):
        
        self.saldo -= valor
        return self.saldo
    
# chamando as funções  
contabancaria= ContaBancaria(12345, "Heres Silva", 1500)
print(contabancaria.deposito(300))
print(contabancaria.saque(500))