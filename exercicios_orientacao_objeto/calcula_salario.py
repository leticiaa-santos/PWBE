# =========================== EXERCICIO 5 =======================
# Crie uma classe chamada “Funcionário” com atributos para armazenar o nome, o 
# salário e o cargo do funcionário. Implemente métodos para calcular o salário líquido, 
# considerando descontos de impostos e benefícios.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        self.IMPOSTO = 64
        self.BENEFICIO = 78

    def descontos(self):
        self.total_descontos = self.IMPOSTO + self.BENEFICIO
        self.salario_final = self.salario - self.total_descontos
        print(f"O funcionário {self.nome}, com o cargo {self.cargo} tem um salário inicial sem descontos de R$ {self.salario} tem {self.total_descontos:,.2f} de descontos e seu salario final com os descontos de {self.salario_final}")

funcionario_1 = Funcionario("Funcionario 1", 3000, "Programador")
funcionario_1.descontos()