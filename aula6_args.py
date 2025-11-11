'''
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''
# Lembre-se de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total+=numero
        
    print(total)

soma(1,2,3,4,5,6)

# Em Python *args (do inglês, arguments) é uma convenção para permitir
# que uma função receba um número variável de argumentos posicionais(sem nome)
# que são agrupados numa tupla dentro da função
# Este recurso é útil quando não se sabe quantos argumentos serão passados para
# a função, como ao somar um número desconhecido de valores.