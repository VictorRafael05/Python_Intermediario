'''
Retorno de valores das funções (return)
'''

def soma(x, y):
    if x > 10:
        return 10    # Se a condição for satisfeita retornará 10 e nao chegará ao outro return, pq só pode retornar um valor na função
    return x + y     # return indica para parar e retornar o valor, entao ele deve estar ao final da função


soma1 = soma(2,2)
soma2 = soma(5,5)
print(soma1+soma2)
