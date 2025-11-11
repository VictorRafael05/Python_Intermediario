import sys 

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()  

lista = [n for n in range(1000000)]  # a lista ja fica toda na memoria
generator = (n for n in range(1000000))   # entre parenteses em vez de colchete fica um generator

print(sys.getsizeof(lista))      # generator nao salva tudo na memoria ao contrario da lista fazendo assim ocupar bem menos espaco
print(sys.getsizeof(generator))  # a biblioteca sys usou o getsizeof para medir quando ocupa da memoria 

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))   # generator é uma funcao que pausa e mostra apenas uma por vez

