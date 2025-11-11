# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:            # sempre comeca com try e nunca poderá estar só
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):        # pode ter quantos except quiser 
    print('NameError, ImportError')
else:                       # quase nunca usado 
    print('Não deu erro')
finally:                    # sempre irá executar o finally
    print('FECHAR ARQUIVO')