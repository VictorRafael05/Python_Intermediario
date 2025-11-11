# raise - lançando exceções (erros)

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True

def dever_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    True

def divide(n, d):
    dever_ser_int_ou_float(n)
    dever_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(8, 's'))