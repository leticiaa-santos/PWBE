# ================= EXERCICIO 2 ====================
# Implemente uma classe chamada “ContaBancária” que possua atributos para 
# armazenar o número da conta, nome do titular e saldo. Adicione métodos para realizar 
# depósitos e saques.

class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo, valor):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.valor = valor

    def depositar(self):
        self.novo_saldo = self.saldo + self.valor # adiciona o valor de depósito ao saldo anterior
        print(f"{self.nome_titular} depositou {self.valor} e tem um saldo de {self.novo_saldo}")

    def sacar(self):
        if self.saldo > 0:
            self.novo_saldo = self.saldo - self.valor # subtrai o valor de depósito ao saldo anterior
            print(f"{self.nome_titular} sacou {self.valor} e tem um saldo de {self.novo_saldo}")
        else:
            print(f"{self.nome_titular} não tem saldo suficiente para sacar dinheiro")


titular_1 = ContaBancaria(1836585-0, "Letícia", 100, 10)
titular_1.depositar()
titular_1.sacar()

titular_2 = ContaBancaria(53958262-00, "Fulano", 0, 100)
titular_2.sacar()
