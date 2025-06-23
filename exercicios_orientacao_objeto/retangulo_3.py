# ====================== EXERCICIO 3 =======================
# Crie uma classe chamada “Retângulo” que possua atributos para armazenar a largura e 
# a altura. Implemente métodos para calcular a área e o perímetro do retângulo

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcula_area(self):
        self.area = self.largura * self.altura # calculo da area do retangulo
        print(f"A área do retângulo é: {self.area}")

    def calcula_perimetro(self):
        self.perimetro = (self.largura * 2) + (self.altura * 2) # calculo do perimetro do retangulo
        print(f"O perímetro do retângulo é: {self.perimetro}")

retangulo = Retangulo(20, 10)
retangulo.calcula_area()
retangulo.calcula_perimetro()