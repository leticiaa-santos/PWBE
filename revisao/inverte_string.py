def inverter_string():

    string = input("Digite uma palavra: ")
    
    string_invertida = ''

    for i in string:
        string_invertida = i + string_invertida
    
    print(string_invertida)

inverter_string()