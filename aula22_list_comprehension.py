# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis. 
# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [numero for numero in range(10)]  # jeito de criar lista em list comprehension
print(lista)                              # o numero a esquerda sera o item adicionado a lista

lista = [
    numero * 2             # é possível fazer alterações na lista 
    for numero in range(10)
         ]
print(lista)