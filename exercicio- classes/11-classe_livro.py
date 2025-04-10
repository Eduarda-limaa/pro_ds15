class Banco:

    def __init__(self):
        self.calculos = {}

    def cadastro_usuario(self, nome, cpf):
        self.calculos[cpf] = {'nome': nome, 'saldo': 0}
        print(f"{nome} cadastrado com sucesso!")

    def abrir_conta(self, cpf, saldo_inicial=0):
        if cpf in self.calculos:
            self.calculos[cpf]['saldo'] = saldo_inicial
            print(f"Conta aberta para {self.calculos[cpf]['nome']} com saldo de R${saldo_inicial}.")
        else:
            print("Cliente não encontrado!")

    def deposito(self, cpf, valor):
        if cpf in self.calculos:
            self.calculos[cpf]['saldo'] += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("Conta não encontrada!")

    def saque(self, cpf, valor):
        if cpf in self.calculos and self.calculos[cpf]['saldo'] >= valor:
            self.calculos[cpf]['saldo'] -= valor
            print(f"Saque de R${valor} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou conta não encontrada.")

    def transferencia(self, cpf_origem, cpf_destino, valor):
        if cpf_origem in self.calculos and cpf_destino in self.calculos and self.calculos[cpf_origem]['saldo'] >= valor:
            self.calculos[cpf_origem]['saldo'] -= valor
            self.calculos[cpf_destino]['saldo'] += valor
            print(f"Transferência de R${valor} realizada com sucesso!")
        else:
            print("Erro na transferência.")

    def exibir_saldo(self, cpf):
        if cpf in self.calculos:
            print(f"Saldo de {self.calculos[cpf]['nome']}: R${self.calculos[cpf]['saldo']}")
        else:
            print("Conta não encontrada.")


# CHAMANDO AS CLASSES
banco = Banco()
banco.cadastro_usuario("Evellyn Maria Silva", "546.555.111-0")

banco.abrir_conta("546.555.111-0", 900)

banco.deposito("546.555.111-0", 200)
banco.saque("546.555.111-0", 100)
banco.transferencia("546.555.111-0", "387.154.021-1", 150)

banco.exibir_saldo("546.555.111-0")
banco.exibir_saldo("387.154.021-1")
