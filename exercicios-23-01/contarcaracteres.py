def contar_caracteres(s):
    contador= {}
    
    for string in s:
        if string in contador:
            contador[string] += 1
        else:
            contador[string] = 1
    return contador

palavra= "Maria"
print(contar_caracteres(palavra))
