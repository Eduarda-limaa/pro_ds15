class Circulo:

    def __init__(self, raio):

        self.raio= raio

    def calcular_area(self):

        area= 3.14 * self.raio ** 2
        return area

    def calcular_perimetro(self):
        
        perimetro= 2 * 3.14 * self.raio
        return perimetro

circulo= Circulo(9)
print(f"A sua área é: {circulo.calcular_area()}")
print(f"O seu perimetro é: {circulo.calcular_perimetro()}")

    

  


