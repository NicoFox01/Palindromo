def palindromo():
    oracion1 = input("Escribe una palabra u oración para averiguar si es un palíndromo: ").lower()
    lista_de_caracteres_derecho = []
    
    for caracter in oracion1:
        if caracter.isalnum():
            lista_de_caracteres_derecho.append(caracter)

    lista_de_caracteres_alreves = lista_de_caracteres_derecho.copy()
    lista_de_caracteres_alreves.reverse()

    if lista_de_caracteres_derecho == lista_de_caracteres_alreves:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")

palindromo()
