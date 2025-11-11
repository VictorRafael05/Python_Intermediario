'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos
externos.
A palavra global faz uma variável do escopo externo ser 
a mesma no escopo interno.
'''

x = 1 

def escopo():             # As funções só podem acessar valores de fora dela
    global x              # Altera o x que vem fora da função
    x = 10                # Esse x não é o mesmo de fora, pq ele esta no escopo interno

    def outra_funcao():   # Valores de dentro de outra função ficam fora do escopo
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

escopo()
print(x)    # Não será alterado, continuará sendo 1 pois o que é mexido dentro da função nao altera o que vem fora dela
