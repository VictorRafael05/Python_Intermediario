'''
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

================= resultado
lista_soma = [2, 4, 6, 8]
'''

# FORMA GERAL DE SE RESOVER, SEM USAR RECURSOS UNICOS DO PYTHON

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = []
for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

# SOLUCAO USANDO RECURSOS PYTHON

lista_soma = []
for i, _ in enumerate(lista_b):    # O UNDERLINE FOI PRA MOSTRAR QUE SO QUEREMOS O VALOR
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

# A MELHOR SOLUCAO SERIA ESSA COM RECURSOS DO PYTHON

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]  # uma list comprehension usando zip para fazer a uniao das duas listas
print(lista_soma)

# AGORA VAMOS SOMAR COM A LISTA DE MAIOR VALOR. IRA FALTAR VALORES E PARA ISSO USAREMOS O fillvalue=0
from itertools import zip_longest   # modulo para pegar a lista de maior valor

lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)] # fillvalue pega os indices sem valor e coloca zero no lugar

print(lista_soma)