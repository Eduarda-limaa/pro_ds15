# iniciando a classe
class Circulo:

    def __init__(self, raio):

        self.raio= raio

# calculando area do circulo
    def calcular_area(self):

        area= 3.14 * self.raio ** 2
        return area

# calculando o perimetro do circulo
    def calcular_perimetro(self):
        
        perimetro= 2 * 3.14 * self.raio
        return perimetro

# chamando as funcoes
circulo= Circulo(9)
print(f"A sua área é: {circulo.calcular_area()}")
print(f"O seu perimetro é: {circulo.calcular_perimetro()}")

    

  


