# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis. 
# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [numero for numero in range(10)]  # jeito de criar lista em list comprehension
# print(lista)                              # o numero a esquerda sera o item adicionado a lista

lista = [
    numero * 2             # é possível fazer alterações na lista 
    for numero in range(10)
         ]
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },               # no dicionario primeiro vem a chave e em seguida ao : vem o valor 
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [                                # criando um novo dicionario desempacotando o anterior
    {**produto, 'preco': produto['preco'] *1.05}  # desempacotamento do dicionario e alteracao do preço
    if produto['preco'] > 20 else {**produto}     # fazendo uma condicao para o aumento do preço, foi colocado o desempacotamento
    for produto in produtos                       # {**produto} ao inves de produto['preco'] para que seja mostrado todo dicionario
]                                                 # o que vem antes do for é considerado mapeamento

print(*novos_produtos, sep='\n')    # desempacotamento da lista e o sep= para quebrar a linha