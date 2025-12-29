# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')  # O * para expandir a lista de deixar menos baguncada e o \n para quebrar a linda no separador
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g']
    ['masculino', 'feminino']
]

print_iter(combinations(pessoas, 2)) # o numero é para falar de quantas pessoas tem no grupo
print_iter(permutations(pessoas, 2)) # o numero é para falar de quantas pessoas tem no grupo

print_iter(product(*camisetas))
