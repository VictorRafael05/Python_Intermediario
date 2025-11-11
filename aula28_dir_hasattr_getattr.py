# dir, hassattr e getattr em Python
string = 'Luiz'
print(string)

if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())

metodo ='lower'

if hasattr(string, metodo):
    print('Existe lower')
    print(getattr(string, metodo)())
else:
    print('Não existe')