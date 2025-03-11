# =================== EXERCICIO 6 ================================
# Implemente uma classe chamada “Produto” que possua atributos para armazenar o 
# nome, o preço e a quantidade em estoque. Adicione métodos para calcular o valor 
# total em estoque e verificar se o produto está disponível.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_estoque(self):
        self.valor_total = self.preco * self.quantidade
        print(f"No estoque tem {self.quantidade} {self.nome} totalizando R$ {self.valor_total:,.2f}")

    def disponivel(self):
        if self.quantidade > 0:
            print(f"Produto {self.nome} está disponível no estoque com {self.quantidade} unidades")
        else:
            print(f"O produto {self.nome} não está disponível")


produto_1 = Produto("Maçã", 3.99, 10)
produto_1.valor_estoque()
produto_1.disponivel()

produto_2 = Produto("Bolo", 9.98, 0)
produto_2.valor_estoque()
produto_2.disponivel()