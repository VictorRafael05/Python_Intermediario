# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))
'''
yield em Python é uma palavra-chave usada em funções para criar geradores. Em vez de retornar um valor e terminar a função (como return), yield pausa a execução, retorna um valor e salva o estado da função. A execução é retomada do ponto onde parou na próxima vez que um valor for solicitado. Isso é útil para otimizar o uso de memória ao processar grandes conjuntos de dados, pois os valores são gerados "sob demanda" e não todos de uma vez. 
'''

def generator(n=0):
    yield 1  # pausar
    print("Continuando...")
    yield 2  # pausar
    print("Mais uma...")
    yield 3
    print("Vou terminar")
    return "ACABOU"

gen = generator(n=0)
print(next(gen))
print(next(gen))   # chama de novo a funcao e continua de onde parou
print(next(gen))   # só irá continuar se tiver como seguir

for n in gen:
    print(n)