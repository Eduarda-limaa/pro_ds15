def inverter_string(s):
    string_invertida = ""

    for char in s:
        string_invertida = char + string_invertida
    return(string_invertida)
    
palavra= "Desejo"
print(inverter_string(palavra))