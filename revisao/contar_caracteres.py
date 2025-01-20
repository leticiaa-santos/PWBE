def contar_caracteres():

    dicionario = {}

    string = input("Informe uma palavra: ")

    for i in string:
        
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1

    print(dicionario)
    
contar_caracteres()