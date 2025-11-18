'''
Closure e funções que retornam outras funções
Em Python, um closure (ou fecho) é uma função que mantém o acesso
 a variáveis do seu escopo (ou ambiente léxico) onde foi criada, 
 mesmo depois que a função externa já terminou de executar. 
 Isto acontece quando definimos uma função aninhada dentro 
 de outra função e retornamos a função interna. 
 Closures são úteis para criar "fábricas de funções", 
 encapsular dados, gerir estados simples e são a base 
 para os decoradores em Python. 
'''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Boa noite')

print(s1('Luiz'))
print(s2('Luiz'))

lista_nomes = ['Victor', 'Emilly', 'Luiz']

for nome in lista_nomes:
    print(s1(nome))
    print(s2(nome))