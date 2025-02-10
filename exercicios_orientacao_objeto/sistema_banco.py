# ======================== EXERCICIO 11 =============================
# Implemente uma classe chamada “Banco” que represente uma instituição financeira.
# Essa classe deve conter métodos para cadastrar clientes, abrir contas bancárias e
# realizar operações como saques, depósitos e transferências.
import os

class Banco:
    def __init__(self):
        self.clientes = []
        self.cliente = {}


    def menu_opcoes(self):
        opcao = input("""O que deseja fazer?
        [1] Abrir conta
        [2] Sacar
        [3] Depositar
        [4] Tranferir
        [5] Sair
        """)

        if opcao == '1':
            self.cadastrar_clientes()
        elif opcao == '2':
            self.sacar()
        elif opcao == '3':
            self.depositar()
        elif opcao == '4':
            self.transferir()
        elif opcao == '5':
            print("Até mais! Obrigado por usar nossos serviços!")
        else:
            print("Opção inválida. Informe um número que esteja no menu de opções")
            self.menu_opcoes()
        os.system('cls')

    def cadastrar_clientes(self):
        print("=============================== Banco ===========================")
        nome = input("Informe seu nome: ")
        cpf = input("Informe seu CPF: ")
        idade = input("Informe sua idade: ")
        senha = input("Informe uma senha: ")
        saldo = 0

        cliente = {'nome' : nome,
                   'CPF' : cpf,
                   'idade' : idade,
                   'senha' : senha,
                   'saldo' : saldo} 
        
        self.clientes.append(cliente)
        
        print(f"Cliente {nome} foi cadastrado com sucesso")
        print(f"É necessário fazer um depósito inicial na conta")
        valor = float(input("Informe o valor que deseja depositar: "))
        cliente ['saldo'] += valor
        print(f"O saldo ficou em R$ {cliente['saldo']}")

        self.menu_opcoes()


    def encontrar_cliente(self, cpf):
            for cliente in self.clientes:
                if cliente ['CPF'] == cpf:
                    return cliente
            return None
    
    
    def sacar(self):
        cpf = input("Informe o seu CPF para sacar: ")
        cliente = self.encontrar_cliente(cpf)

        if cliente: 
            valor = float(input("Informe o valor que deseja sacar: "))
            if cliente ['saldo'] >= valor:
                cliente ['saldo'] -= valor
                print(f"O saque de R$ {valor} foi realizado com sucesso! O seu saldo atual é R$ {cliente['saldo']}")
                
            else:
                print(f"{cliente['nome']} não tem saldo suficiente para sacar")
        else:
            print("O CFP informado não está cadastrado, informe dados válidos para realizar o saque!")
        
        self.menu_opcoes()


    def depositar(self):
        cpf = input("Informe o seu CPF para depositar: ")
        cliente = self.encontrar_cliente(cpf)

        if cliente:
            valor = float(input("Informe o valor que deseja sacar: "))
            cliente ['saldo'] += valor
            print(f"O deposito de R$ {valor} foi realizado com sucesso! O seu saldo atual é R$ {cliente['saldo']}")
        else:
            print("O CFP informado não está cadastrado, informe dados válidos para realizar o saque!")

        self.menu_opcoes()

        
    def transferir(self):
        cpf_origem = input("Informe o seu CPF para transferir: ")
        conta_origem = self.encontrar_cliente(cpf_origem)
        
        if conta_origem:
            cpf_destino = input("Informe o CPF da pessoa que deseja realizar a transferência: ")
            conta_destino = self.encontrar_cliente(cpf_destino)

            if conta_destino:
                valor = float(input("Informe o valor que deseja transferir: "))
                if conta_origem ['saldo'] >= valor:
                    conta_origem ['saldo'] -= valor
                    conta_destino ['saldo'] += valor
                    print(f"A transferência no valor de R$ {valor} foi realizado com sucesso!")
                    print(f"{conta_origem['nome']} seu saldo atual da sua conta é R$ {conta_origem['saldo']}")
                    print(f"{conta_destino['nome']} seu saldo atual da conta é R$ {conta_destino['saldo']}")
                else:
                    print("Valor do saldo da conta insuficiente para realizar a transferência")
            else:
                print("O CPF informado não está correto")
        else:
            ("O CPF informado não está correto")
        
        self.menu_opcoes()
        
        

banco = Banco()
banco.menu_opcoes()