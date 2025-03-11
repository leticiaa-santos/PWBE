# ========================= EXERCICIO 7 ========================
# Crie uma classe chamada “Triângulo” com atributos para armazenar os três lados do 
# triângulo. Implemente métodos para verificar se é um triângulo válido e calcular sua 
# área.

class Triangulo:
    def __init__(self, lado_1, lado_2, lado_3, base, altura):
        self.lado_1 = lado_1
        self.lado_2 = lado_2
        self.lado_3 = lado_3
        self.base = base
        self.altura = altura

    def verifica_triangulo(self):
        if self.lado_1 + self.lado_2 > self.lado_3 and self.lado_1 + self.lado_3 > self.lado_2 and self.lado_2 + self.lado_3 > self.lado_1:
            print("Triângulo Válido")
        else:
            print("Triângulo inválido")

    def calcula_area(self):
        self.area = (self.base * self.altura) / 2
        print(f"A área do triângulo {self.area}")

traingulo_1 = Triangulo(3, 4, 5, 4, 3)
traingulo_1.verifica_triangulo()
traingulo_1.calcula_area()

traingulo_2 = Triangulo(100, 103, 2, 10, 2)
traingulo_2.verifica_triangulo()
traingulo_2.calcula_area()