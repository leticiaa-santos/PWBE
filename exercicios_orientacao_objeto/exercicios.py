# =============== EXERCICIO 1 ======================
# Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio e 
# métodos para calcular a área e o perímetro do círculo.

# class Circulo:
#     def __init__(self, raio):
#         self.raio = raio
#         self.PI = 3.14

#     def calcula_arera(self):
#         self.area_circulo = self.PI * (self.raio ** 2)
#         print(f"A área do circulo é igual a {self.area_circulo:,.2f}")

#     def calcula_perimetro(self):
#         self.perimetro_circulo = (2 * self.PI) * self.raio
#         print(f"O perimetro do circulo é igual a {self.perimetro_circulo:,.2f}")

# circulo = Circulo(10)

# circulo.calcula_arera()
# circulo.calcula_perimetro()

# ================= EXERCICIO 2 ====================
# Implemente uma classe chamada “ContaBancária” que possua atributos para 
# armazenar o número da conta, nome do titular e saldo. Adicione métodos para realizar 
# depósitos e saques.

# class ContaBancaria:
#     def __init__(self, numero_conta, nome_titular, saldo, valor):
#         self.numero_conta = numero_conta
#         self.nome_titular = nome_titular
#         self.saldo = saldo
#         self.valor = valor

#     def depositar(self):
#         self.novo_saldo = self.saldo + self.valor
#         print(f"{self.nome_titular} depositou {self.valor} e tem um saldo de {self.novo_saldo}")

#     def sacar(self):
#         if self.saldo > 0:
#             self.novo_saldo = self.saldo - self.valor
#             print(f"{self.nome_titular} sacou {self.valor} e tem um saldo de {self.novo_saldo}")
#         else:
#             print(f"{self.nome_titular} não tem saldo suficiente para sacar dinheiro")


# titular_1 = ContaBancaria(1836585-0, "Letícia", 100, 10)
# titular_1.depositar()
# titular_1.sacar()

# titular_2 = ContaBancaria(53958262-00, "Fulano", 0, 100)
# titular_2.sacar()


# ====================== EXERCICIO 3 =======================
# Crie uma classe chamada “Retângulo” que possua atributos para armazenar a largura e 
# a altura. Implemente métodos para calcular a área e o perímetro do retângulo

# class Retangulo:
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura

#     def calcula_area(self):
#         self.area = self.largura * self.altura
#         print(f"A área do retângulo é: {self.area}")

#     def calcula_perimetro(self):
#         self.perimetro = (self.largura * 2) + (self.altura * 2)
#         print(f"O perímetro do retângulo é: {self.perimetro}")

# retangulo = Retangulo(20, 10)
# retangulo.calcula_area()
# retangulo.calcula_perimetro()


# ============= EXERCICIO 4 ========================
# Implemente uma classe chamada “Aluno” que possua atributos para armazenar o 
# nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média das 
# notas e verificar a situação do aluno (aprovado ou reprovado).

# class Aluno:
#     def __init__(self, nome, matricula, nota1, nota2, nota3):
#         self.nome = nome
#         self.matricula = matricula
#         self.nota1 = nota1
#         self.nota2 = nota2
#         self.nota3 = nota3

#     def calcular_media(self):
#         self.media = (self.nota1 + self.nota2 + self.nota3) / 3
#         print(f"{self.nome} ficou com média: {self.media:,.2f}")

#     def verificar_situacao(self):
#         if self.media > 5.0:
#             print("Aluno aprovado")
#         else:
#             print("Aluno reprovado")

# aluno_1 = Aluno("Aluno 1", 12345, 10, 9.5, 8)
# aluno_1.calcular_media()
# aluno_1.verificar_situacao()

# aluno_2 = Aluno("Aluno 2", 98765, 2, 1.5, 3)
# aluno_2.calcular_media()
# aluno_2.verificar_situacao()


# =========================== EXERCICIO 5 =======================
# Crie uma classe chamada “Funcionário” com atributos para armazenar o nome, o 
# salário e o cargo do funcionário. Implemente métodos para calcular o salário líquido, 
# considerando descontos de impostos e benefícios.

# class Funcionario:
#     def __init__(self, nome, salario, cargo):
#         self.nome = nome
#         self.salario = salario
#         self.cargo = cargo
#         self.IMPOSTO = 64
#         self.BENEFICIO = 78

#     def descontos(self):
#         self.total_descontos = self.Imposto + self.Beneficio
#         self.salario_final = self.salario - self.total_descontos
#         print(f"O funcionário {self.nome}, com o cargo {self.cargo} tem um salário inicial sem descontos de R$ {self.salario} tem {self.total_descontos:,.2f} de descontos e seu salario final com os descontos de {self.salario_final}")

# funcionario_1 = Funcionario("Funcionario 1", 3500.65, "Programador")
# funcionario_1.descontos()


# =================== EXERCICIO 6 ================================
# Implemente uma classe chamada “Produto” que possua atributos para armazenar o 
# nome, o preço e a quantidade em estoque. Adicione métodos para calcular o valor 
# total em estoque e verificar se o produto está disponível.

# class Produto:
#     def __init__(self, nome, preco, quantidade):
#         self.nome = nome
#         self.preco = preco
#         self.quantidade = quantidade

#     def valor_estoque(self):
#         self.valor_total = self.preco * self.quantidade
#         print(f"No estoque tem {self.quantidade} {self.nome} totalizando R$ {self.valor_total:,.2f}")

#     def disponivel(self):
#         if self.quantidade > 0:
#             print(f"Produto {self.nome} está disponível no estoque com {self.quantidade} unidades")
#         else:
#             print(f"O produto {self.nome} não está disponível")


# produto_1 = Produto("Maçã", 3.99, 10)
# produto_1.valor_estoque()
# produto_1.disponivel()

# produto_2 = Produto("Bolo", 9.98, 0)
# produto_2.valor_estoque()
# produto_2.disponivel()


# ========================= EXERCICIO 7 ========================
# Crie uma classe chamada “Triângulo” com atributos para armazenar os três lados do 
# triângulo. Implemente métodos para verificar se é um triângulo válido e calcular sua 
# área.

# class Triangulo:
#     def __init__(self, lado_1, lado_2, lado_3, base, altura):
#         self.lado_1 = lado_1
#         self.lado_2 = lado_2
#         self.lado_3 = lado_3
#         self.base = base
#         self.altura = altura

#     def verifica_triangulo(self):
#         if self.lado_1 + self.lado_2 > self.lado_3 and self.lado_1 + self.lado_3 > self.lado_2 and self.lado_2 + self.lado_3 > self.lado_1:
#             print("Triângulo Válido")
#         else:
#             print("Triângulo inválido")

#     def calcula_area(self):
#         self.area = (self.base * self.altura) / 2
#         print(f"A área do triângulo {self.area}")

# traingulo_1 = Triangulo(3, 4, 5, 4, 3)
# traingulo_1.verifica_triangulo()
# traingulo_1.calcula_area()

# traingulo_2 = Triangulo(100, 103, 2, 10, 2)
# traingulo_2.verifica_triangulo()
# traingulo_2.calcula_area()


#======================= EXERCICIO 8 ==========================
# Implemente uma classe chamada “Carro” com atributos para armazenar a marca, o 
# modelo e a velocidade atual do carro. Adicione métodos para acelerar, frear e exibir a 
# velocidade atual.

# class Carro:
#     def __init__(self, marca, modelo, velocidade_atual, mudar_velocidade):
#         self.marca = marca
#         self.modelo = modelo
#         self.velocidade_atual = velocidade_atual
#         self.mudar_velocidade = mudar_velocidade

#     def acelerar_carro(self):
#         self.acelerar = self.velocidade_atual + self.mudar_velocidade
#         print(f"A velocidade do carro era {self.velocidade_atual} você acelerou {self.mudar_velocidade}, a velocidade atual é: {self.acelerar}")

#     def frear_carro(self):
#         if self.velocidade_atual <= 0:
#             print("O carro já está parado, não é possível frear")
#         else:
#             self.frear = self.velocidade_atual - self.mudar_velocidade
#             print(f"A velocidade do carro era {self.velocidade_atual} você freou {self.mudar_velocidade}, a velocidade atual é: {self.frear}")

# carro_1 = Carro("marca_1", "modelo_1", 100, 10)
# carro_1.acelerar_carro()
# carro_1.frear_carro()

# carro_2 = Carro("marca_2", "modelo_2", 0, 20)
# carro_2.frear_carro()
# carro_2.acelerar_carro()


# ==================== EXERCICIO 9 ==============================
# Crie uma classe chamada “Paciente” que possua atributos para armazenar o nome, a 
# idade e o histórico de consultas de um paciente. Implemente métodos para adicionar 
# uma nova consulta ao histórico e exibir as consultas realizadas

# class Paciente:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#         self.historico = []

#     def nova_consulta(self, consulta):
#         self.historico.append(consulta)

#     def mostrar_historico(self):
#         if not self.historico:
#             print(f"O paciente {self.nome} ainda não tem nenhuma consulta")
#         else:
#             print(f"O paciente {self.nome} possui as consultas: ")
#             for i, consulta in enumerate(self.historico, 1):
#                 print(f"{i} - {consulta}")


# paciente_1 = Paciente("Paciente 1", 10)
# paciente_1.nova_consulta("Pediatra")
# paciente_1.nova_consulta("Ortopedista")
# paciente_1.mostrar_historico()


# =========================== EXERCICIO 10 ===============================
# Implemente uma classe chamada “Livro” com atributos para armazenar o título, o
# autor e o número de páginas do livro. Adicione métodos para emprestar o livro,
# devolvê-lo e verificar se está disponível.

# class Livro:
#     def __init__(self, titulo, autor, paginas):
#         self.titulo = titulo
#         self.autor = autor
#         self.paginas = paginas
#         self.livro_disponivel = True

#     def emprestar_livro(self):
#         if self.livro_disponivel:
#             self.livro_disponivel = False
#             print(f"Parabéns, você pegou emprestado o livro {self.titulo}")
#         else:
#             print(f"O livro {self.titulo} não está disponível para empréstimo no momento")

#     def devolver_livro(self):
#         if not self.livro_disponivel:
#             self.livro_disponivel = True
#             print(f"Você devolveu o livro {self.titulo} com sucesso")
#         else:
#             print("O livro já foi devolvido, essa operação não pode ser realizada")

#     def verificar_disponibilidade(self):
#         if self.livro_disponivel:
#             print(f"O livro {self.titulo} está disponível")
#         else:
#             print(f"O livro {self.titulo} não está disponível")


# livro_1 = Livro("Crepusculo", "stephanie mayer", 324)
# livro_1.emprestar_livro()
# livro_1.verificar_disponibilidade()
# livro_1.devolver_livro()
# livro_1.verificar_disponibilidade()

# ======================== EXERCICIO 11 =============================
# Implemente uma classe chamada “Banco” que represente uma instituição financeira.
# Essa classe deve conter métodos para cadastrar clientes, abrir contas bancárias e
# realizar operações como saques, depósitos e transferências.

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


    def cadastrar_clientes(self):
        print("=============================== Banco ===========================")
        nome = input("Informe seu nome: ")
        cpf = input("Informe seu CPF: ")
        idade = input("Informe sua idade: ")
        senha = input("Informe uma senha")
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

    def sacar(self):
        cpf = input("Informe o seu CPF para sacar: ")
        cliente = self.encontrar_cliente(cpf)

        if cliente: 
            if cliente ['saldo'] == 0:
                print(f"{cliente['nome']} não tem saldo suficiente para sacar")
        
        

banco = Banco()
banco.menu_opcoes()
