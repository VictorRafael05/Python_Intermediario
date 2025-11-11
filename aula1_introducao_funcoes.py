'''
Introdução as funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
'''

def imprimir(a, b, c):    # os valores dentro sao chamados de parametros
    print('Várias1')
    print('Várias2')
    print('Várias3')
    print('Várias4')
    print(a, b, c)

imprimir(1, 2, 3)        # agora os valores que eu devo colocar são argumentos para os parametros criados
imprimir(9, 8, 7)

def saudacao(nome='Sem nome'):
    print(f'Olá {nome}!')

saudacao('Victor')
saudacao('Emilly')
saudacao()   # Se eu nao passar nada provocaria um erro mas foi colocado 'Sem nome'
             # desse jeito se nao passar nenhum valor ficara como Sem nome