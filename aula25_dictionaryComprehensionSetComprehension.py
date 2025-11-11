# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
}

dc = {
    chave: valor
    for chave, valor
    in produto.items()
}

print(dc)

# Set Comprehension

s1 = {i for i in range(10)}
print(s1)