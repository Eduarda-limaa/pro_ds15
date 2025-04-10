# importando o metodo de calculo
import math

# iniciando a classe
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

# verificando os lados do triangulo 
    def calculo(self):
        if self.lado1 < (self.lado2 + self.lado3) and self.lado2 < (self.lado1 + self.lado3) and self.lado3 < (self.lado1 + self.lado2):
            return True
        else: 
            return False
            

    def area(self):
        if self.calculo():
            perimetro = self.lado1 + self.lado2 + self.lado3
            semi = perimetro / 2
            area = math.sqrt(semi*(semi-self.lado1)*(semi-self.lado2)*(semi-self.lado3))
            print(area)
            print("O triangulo é válido")
        else:
            print("Não foi possível fazer a conta. Coloque um valor valido.")

triangulo = Triangulo(4, 5, 2)
triangulo.calculo()
triangulo.area()


# o math.sqrt = conta matematica
