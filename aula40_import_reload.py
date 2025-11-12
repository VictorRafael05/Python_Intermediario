# O modulo Python so é carregado uma vez para mais vezes tem que usar importlib
import importlib   # Para poder usar o reload
               
import aula40_m

print(aula40_m.variavel)

for i in range(10):
    importlib.reload(aula40_m)  # O modulo so sera recarregado se for solicitado
    print(i) 

print("Fim.")