def merge_sort(lista):

    if len(lista) <=1:
        return lista
    

# divisão da lista

    metade= len(lista) //2
    esquerda= lista[:metade]
    direita= lista[metade:]

    esquerda= merge_sort(esquerda)
    direita= merge_sort(direita)
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    a, b = 0, 0

    while a < len(esquerda) and b < len(direita):
        if esquerda[a] < direita[b]:
            resultado.append(esquerda[a])
            a += 1

        else: 
            resultado.append(direita[b])
            b += 1

    while a < len(esquerda):
        resultado.append(esquerda[a])
        a += 1

    while b < len(direita):
        resultado.append(direita[b])
        b += 1

    return resultado

lista= [56, 9, 10, 24, 5]
lista_pronta= merge_sort(lista)
print(lista_pronta)