# Try, except, else e finally

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[10])
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError):   # para colocar mais de um erro se faz uma tupla
    print('TypeError + IndexError')
    
except Exception:
    print('ERRO DESCONHECIDO')   #Maior classe de erro

print('CONTINUAR')