# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(intervalo_maximo)
    ]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1, l2))

#### JÁ EXISTE NO PYTHON UMA FORMA DE SER RESOLVIDO ####

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(lista1, lista2)))   # ESSA É  A FORMA JA EXISTENTE PARA UNIR LISTAS NO PYTHON


# PARA USAR A LISTA MAIOR EXISTE UM MODULO PARA SER USADO A LISTA MAIOR O itertools zip_longest

from itertools import zip_longest

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip_longest(lista1, lista2, fillvalue='Sem Cidade'))) # PARA SUPRIR ONDE NÃO HÁ VALORES COLOCAMOS UM fillvalue