# =========================== EXERCICIO 10 ===============================
# Implemente uma classe chamada “Livro” com atributos para armazenar o título, o
# autor e o número de páginas do livro. Adicione métodos para emprestar o livro,
# devolvê-lo e verificar se está disponível.

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.livro_disponivel = True

    def emprestar_livro(self):
        if self.livro_disponivel:
            self.livro_disponivel = False
            print(f"Parabéns, você pegou emprestado o livro {self.titulo}")
        else:
            print(f"O livro {self.titulo} não está disponível para empréstimo no momento")

    def devolver_livro(self):
        if not self.livro_disponivel:
            self.livro_disponivel = True
            print(f"Você devolveu o livro {self.titulo} com sucesso")
        else:
            print("O livro já foi devolvido, essa operação não pode ser realizada")

    def verificar_disponibilidade(self):
        if self.livro_disponivel:
            print(f"O livro {self.titulo} está disponível")
        else:
            print(f"O livro {self.titulo} não está disponível")


livro_1 = Livro("Crepusculo", "stephanie mayer", 324)
livro_1.emprestar_livro()
livro_1.verificar_disponibilidade()
livro_1.devolver_livro()
livro_1.verificar_disponibilidade()