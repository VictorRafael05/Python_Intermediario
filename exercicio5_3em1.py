# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos produtos por deep copy (cópia profunda)
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente ( do maior para o menor)
# Gere produtos ordenados por nome por deep copy

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key= lambda p: p['nome'],
    reverse=True
)
print()
print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos ordenados por preço por deep copy

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key= lambda p: p['preco']
    
)
print()
print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')