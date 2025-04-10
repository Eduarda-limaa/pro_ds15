class Carro:
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    def aumentar(self, aumento):
        self.velocidade +=aumento
        print(f"A nova velocidade é: {self.velocidade}")

    def freiar(self, freio):
        self.velocidade -= freio
        print(f"A nova velocidade é: {self.velocidade}")

    

carro = Carro('honda', '1918', 70)
carro.aumentar(20)
carro.freiar(10)