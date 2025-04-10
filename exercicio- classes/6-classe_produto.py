# iniciando as classes
class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome= nome
        self.preco= preco
        self.quantidade= quantidade

# calculando a quantidade de produtos disponiveis
    def calculo(self):
        quantidade= self.quantidade

        if quantidade == 0:
            print("Produto indisponível")
        else:
            print(f"Produto disponível: {self.quantidade}")


# chamando as funções
produto= Produto("Condicionador", 15, 5)
produto.calculo()