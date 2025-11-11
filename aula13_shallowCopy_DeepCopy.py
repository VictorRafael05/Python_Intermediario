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

import copy             # Para fazer um Deepcopy é preciso importar a biblioteca copy que tbm possui o copy normal
                        # mas para usar o deep copy escreve-se copy.deepcopy()

d1 = {
    'c1' : 1,
    'c2' : 2,
    'l1' : [0, 1, 2],
}
d2 = d1.copy()      # Uma cópia rasa que so copia os valores imutaveis
                    # Nos valores de uma lista que é mutável ele so leva ao mesmo local onde a lista está
                    # e mudando o valor da lista do d1 tbm mudará na lista do d2
d3 = copy.deepcopy(d1)   # aqui temos uma copia profunda sem afetar os itens mutaveis
d2['c1'] = 1000
d2['l1'][1] = 99999
d3['l1'][1] = 300
print(d1)
print(d2)
print(d3)
