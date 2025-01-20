nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))
nota_3 = float(input("Digite a nota 3: "))
nota_4 = float(input("Digite a nota 4: "))
nota_5 = float(input("Digite a nota 5: "))

media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5

if media >= 5:
    print(f"Aluno aprovado com a média: {media:,.2f}")
elif media < 5 and media > 2.5:
    print(f"Aluno em recupeção com as média: {media:,.2f}")
else:
    print(f"Aluno reprovado com a média {media:,.2f}")