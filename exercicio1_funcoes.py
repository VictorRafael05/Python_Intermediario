# Exercício com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicando(*args):
    total = 1
    for numero in args:
        total = total * numero
    return total

mult_1 = multiplicando(5, 10, 2)
print(mult_1)



# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(x):
    resultado = x % 2
    if resultado == 0:
        return f'{x} é Par'
    return f'{x} é Ímpar'    # Não precisa do else, pois ele seria redundante, pq o return ja encerra a função

print(par_impar(56))
print(par_impar(101))
