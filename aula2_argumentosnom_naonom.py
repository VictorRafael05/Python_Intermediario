'''
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o arumento (valor)
'''

def soma(x, y):
    print(f'{x=} y={y}', '|', 'x + y = ', x + y)  # Colocar x= entre as chaves mostra a variavel mais o valor dela

soma(1, 2)       # Argumentos não nomeados seguem a ordem 
soma(y=2, x=1)   # Já os argumentos nomeados segue conforme os parâmetros
                 # Toda vez que eu nomear um argumento é preciso nomear todos os próximos
