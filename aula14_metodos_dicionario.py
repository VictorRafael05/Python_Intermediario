# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome' : 'Luiz',
    'sobrenome' : 'Miranda',
}

# print(p1.get('idade', 'Não existe'))

# nome = p1.pop('nome')    # pop apaga a chave 
# print(nome)
# print(p1)

# p1.update({
#     'nome' : 'novo valor',      # update tanto atualiza valores
#     'idade' : 35,               # como pode adicionar novas chaves
# })

# p1.update(nome= 'novo valor', idade= 35)    # uma outra forma de fazer update

# tupla = (('nome', 'novo valor'), ('idade', 35))
lista = [['nome', 'novo valor'], ['idade', 35]]   # tambem é possivel alterar usando listas e tuplas
p1.update(lista)
print(p1)