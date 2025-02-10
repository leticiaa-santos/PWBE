# =============== EXERCICIO 1 ======================
# Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio e 
# métodos para calcular a área e o perímetro do círculo.

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.PI = 3.14

    def calcula_arera(self):
        self.area_circulo = self.PI * (self.raio ** 2)
        print(f"A área do circulo é igual a {self.area_circulo:,.2f}")

    def calcula_perimetro(self):
        self.perimetro_circulo = (2 * self.PI) * self.raio
        print(f"O perimetro do circulo é igual a {self.perimetro_circulo:,.2f}")

circulo = Circulo(10)

circulo.calcula_arera()
circulo.calcula_perimetro()