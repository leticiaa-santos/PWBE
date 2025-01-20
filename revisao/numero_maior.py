numero = 0

maior = 0 

while numero > -1:
    numero = int(input("Digite um número: "))

    if numero > maior:
        maior = numero

print(f"O maior número digitado é: {maior}")

    