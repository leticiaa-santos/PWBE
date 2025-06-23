# =============================== EXERCICIO 17 ==================================
# Implemente uma classe chamada “Biblioteca” que represente uma biblioteca virtual. 
# Essa classe deve permitir cadastrar livros, fazer empréstimos, devolver livros e verificar 
# a disponibilidade de um livro.

class Biblioteca:
    def __init__(self):
        self.livro_disponivel = True
        self.livros = [] 

    def menu(self):
        opcao = input("""O que deseja fazer?
        [1] Cadastrar livros
        [2] Emprestar livro
        [3] Devolver livro
        [4] Verificar a disponibilidade
        [5] Sair
        """)

        if opcao == '1':
            self.cadastrar_livro()
        elif opcao == '2':
            self.emprestar_livro()
        elif opcao == '3':
            self.devolver_livro()
        elif opcao == '4':
            self.verificar_disponibilidade()
        elif opcao == '5':
            print("Estamos encerrando...")
        else:
            print("Essa opção não é válida!")
            self.menu()

    def cadastrar_livro(self):
        print("=========================== Loja Virtual ===========================")
        titulo = input("Informe o titulo do livro: ")
        autor = input("Informe o autor do livro: ")
        paginas = int(input("Informe a quantidade de páginas: "))
        
        livro = {
            'titulo': titulo, 
            'autor': autor, 
            'paginas': paginas
        }
        
        self.livros.append(livro) 

        print(f"\nO livro foi cadastrado: \nTítulo: {livro['titulo']} \nAutor: {livro['autor']} \nPágina: {livro['paginas']}")

        self.menu()

    def emprestar_livro(self):
        if not self.livros:  
            print("Não há livros cadastrados para emprestar.")
            self.menu()
            return
        
        print("Livros disponíveis:")
        for livro in self.livros:
            print(f"- {livro['titulo']}")

        
        titulo = input("Digite o título do livro que deseja emprestar: ")
        livro_encontrado = None 
        

        for livro in self.livros:
            if livro['titulo'].lower() == titulo.lower():
                livro_encontrado = livro
               
                break
        
        if livro_encontrado and self.livro_disponivel:
            self.livro_disponivel = False
            print(f"Parabéns, você pegou emprestado o livro {livro_encontrado['titulo']}")
        elif livro_encontrado:
            print(f"O livro {livro_encontrado['titulo']} não está disponível para empréstimo no momento.")
        else:
            print("Livro não encontrado.")

        self.menu()

    def devolver_livro(self):
        if self.livro_disponivel:
            print("Você não pegou nenhum livro emprestado ainda.")
        else:
            self.livro_disponivel = True
            print("Você devolveu o livro com sucesso.")
        
        self.menu()

    def verificar_disponibilidade(self):
        if self.livros:
            print("Livros disponíveis:")
            for livro in self.livros:
                disponibilidade = "disponível" if self.livro_disponivel else "indisponível"
                print(f"{livro['titulo']} - {disponibilidade}")
        else:
            print("Não há livros cadastrados.")
        
        self.menu()


livro_1 = Biblioteca()
livro_1.menu()
