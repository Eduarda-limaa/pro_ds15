# iniciando a classe
class Retangulo:

    def __init__(self, altura, largura):

        self.altura= altura
        self.largura= largura


# calculando a area do retangulo
    def calcular_area(self):

        area= self.altura * self.largura
        return area

# calculando o perimetro do retangulo
    def calcular_perimetro(self):
        
        perimetro= 2 * (self.altura + self.largura)
        return perimetro

# chamando as funções
retangulo= Retangulo(4, 9)
print(f"A sua área é: {retangulo.calcular_area()}")
print(f"O seu perimetro é: {retangulo.calcular_perimetro()}")

    