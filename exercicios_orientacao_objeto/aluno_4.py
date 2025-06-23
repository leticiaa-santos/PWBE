# ============= EXERCICIO 4 ========================
# Implemente uma classe chamada “Aluno” que possua atributos para armazenar o 
# nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média das 
# notas e verificar a situação do aluno (aprovado ou reprovado).

class Aluno:
    def __init__(self, nome, matricula, nota1, nota2, nota3):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_media(self):
        self.media = (self.nota1 + self.nota2 + self.nota3) / 3 # calculando a média das notas
        print(f"{self.nome} ficou com média: {self.media:,.2f}")

    def verificar_situacao(self):
        if self.media > 5.0: # verificando o valor da média para mostrar a situacao
            print("Aluno aprovado")
        else:
            print("Aluno reprovado")

aluno_1 = Aluno("Aluno 1", 12345, 10, 9.5, 8)
aluno_1.calcular_media()
aluno_1.verificar_situacao()

aluno_2 = Aluno("Aluno 2", 98765, 2, 1.5, 3)
aluno_2.calcular_media()
aluno_2.verificar_situacao()
