'''
Valores padrão para parâmetros 
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
'''
                             # importante definir um valor em caso de edicao de código para evitar bugs
def soma(x, y, z=None):      # None é um não valor 
    if z is not None:        # É necessário colocar is not pois senão ao colocar zero que tbm é falso nao apareceria o valor 
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 4)
soma(100, 200)
soma(7, 9, 0)