# Manipulando chaves e valores em dicionários 
pessoa = {}

pessoa['nome'] = 'Luiz Otávio'     # Criou uma chave no dicionário

chave_dinamica = 'sobrenome'       # Também se pode criar chaves dinamicas atribuindo valores 
pessoa[chave_dinamica] = 'Miranda'     

print(pessoa)

del pessoa['sobrenome']          # Também é possível apagar uma chave usando del

print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('Não Existe')
else:
    print(pessoa['sobrenome'])