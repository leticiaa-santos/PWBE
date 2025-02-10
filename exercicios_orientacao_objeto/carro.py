#======================= EXERCICIO 8 ==========================
# Implemente uma classe chamada “Carro” com atributos para armazenar a marca, o 
# modelo e a velocidade atual do carro. Adicione métodos para acelerar, frear e exibir a 
# velocidade atual.

class Carro:
    def __init__(self, marca, modelo, velocidade_atual, mudar_velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual
        self.mudar_velocidade = mudar_velocidade

    def acelerar_carro(self):
        self.acelerar = self.velocidade_atual + self.mudar_velocidade
        print(f"A velocidade do carro era {self.velocidade_atual} você acelerou {self.mudar_velocidade}, a velocidade atual é: {self.acelerar}")

    def frear_carro(self):
        if self.velocidade_atual <= 0:
            print("O carro já está parado, não é possível frear")
        else:
            self.frear = self.velocidade_atual - self.mudar_velocidade
            print(f"A velocidade do carro era {self.velocidade_atual} você freou {self.mudar_velocidade}, a velocidade atual é: {self.frear}")

carro_1 = Carro("marca_1", "modelo_1", 100, 10)
carro_1.acelerar_carro()
carro_1.frear_carro()

carro_2 = Carro("marca_2", "modelo_2", 0, 20)
carro_2.frear_carro()
carro_2.acelerar_carro()