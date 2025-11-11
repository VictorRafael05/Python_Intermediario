perguntas = [
    {
        'Pergunta' : 'Quanto é 2+2?',
        'Opções' : ['1', '2', '3', '4', '5'],
        'Resposta' : '4'
    },
    {
        'Pergunta' : 'Quanto é 5*5?',
        'Opções' : ['25', '55', '10', '51'],
        'Resposta' : '25',
    },
    {
        'Pergunta' : 'Quanto é 10/2?',
        'Opções' : ['4', '5', '2', '1'],
        'Resposta' : '5',
    },
]

contador_acertos = 0

for pergunta in perguntas:
    
    print(f'Pergunta: {pergunta['Pergunta']}')
    print()
    opcoes = pergunta['Opções']
    for i, item in enumerate(opcoes):
        print(f'{i}) {item}')
    print()

    escolha = input('Digite o item da opção correta: ')
    
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        contador_acertos += 1
        print('Acertou!')
    else:
        print('Errou.')

print()
print(f'Você acertou {contador_acertos} de {len(perguntas)} perguntas.')
    



    



print(f'Total de acertos {contador_acertos} de 3 perguntas')

