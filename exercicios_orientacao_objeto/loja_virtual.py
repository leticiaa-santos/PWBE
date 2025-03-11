#=========================== EXERCICIO 12 ==========================

# Crie uma classe chamada “LojaVirtual” que represente uma plataforma de vendas 
# online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho de 
# compras, aplicar descontos e calcular o valor total da compra.

class LojaVirtual:
    def __init__(self):
        self.produtos = []
        self.carrinho = []
    

    def menu(self):
        opcao = input("""O que deseja fazer?
        [1] Cadastrar produtos
        [2] Adicionar ao carrinho
        [3] Ver carrinho
        [4] Calcular total
        [5] Sair
        """)

        if opcao == '1':
            self.cadastrar_produtos()
        elif opcao == '2':
            self.adicionar_carrinho()
        elif opcao == '3':
            self.ver_carrinho()
        elif opcao == '4':
            self.calcular_total()
        elif opcao == '5':
            print("Estamos encerrando...")
        else:
            print("Essa opção não é valida!")
            self.menu()

    def cadastrar_produtos(self):
        print("=========================== Loja Virtual ===========================")
        nome = input("Informe o nome do produto: ")
        preco = float(input("Informe o preço do produto: "))
        desconto = float(input("Informe o desconto em %: "))
        quantidade = int(input("Informe a quantidade do produto: "))
        
        desconto = desconto / 100
        preco_desconto = preco - (preco * desconto)

        produto = {'nome' : nome,
                   'preco' : preco_desconto,
                   'quantidade' : quantidade,
                   'desconto' : desconto} 
        
        self.produtos.append(produto)

        print(f"\nO produto foi cadastrado: \nNome: {produto['nome']} \nQuantidade: {produto['quantidade']} \nPreço: {produto['preco']:,.2f} ")

        self.menu()

    def adicionar_carrinho(self):
        print("========================== Produtos disponíveis =============================")
        print(self.produtos)
        print("Esses são os produtos disponíveis: ")
        if self.produtos:
            for i, produto in enumerate(self.produtos, 1):
                print(f"\nProduto {i} \n- Nome: {produto['nome']} \n- R$ {produto['preco']} \n- quantidade: {produto['quantidade']}")
        else:
            print("Ainda não há nenhum produto cadastrado")

        escolha_produto = int(input("Qual produto deseja adicionar ao seu carrinho? Digite o numero do produto: "))

        if escolha_produto:
            produto_escolhido = self.produtos[escolha_produto]
            quantidade = int(input(f"Quantas unidades do produto {produto['nome']} você deseja adicionar? "))

            if quantidade <= produto_escolhido['quantidade']:
                self.carrinho.append({'nome' : produto_escolhido['nome'],
                                      'preco' : produto_escolhido['preco'],
                                      'quantidade' : quantidade})
                
                produto_escolhido['quantidade'] -= quantidade
                print(f"Foram adicionadas {quantidade} do produto {produto['nome']} ao seu carrinho")
            else:
                print("Essa quantidade não está disponível em estoque")
        else:
            print("Esse produto não é válido")

        self.menu()

    def ver_carrinho(self):
        print("========================== Seu carrinho =============================")
        if self.carrinho:
            print("Esses são os itens do seu carrinho: ")
            for item in self.carrinho:
                print(f"{item['nome']} - {item['quantidade']} unidades - {item['preco']:,.2f}")
        else:
            print("O carrinho está vazio")

    def calcular_total(self):
            valor_total = sum(item['preco'] * item['quantidade']for item in self.carrinho)
            print(f"O valor total da compra é R$ {valor_total:,.2f}")

            self.menu()

produto = LojaVirtual()
produto.menu()