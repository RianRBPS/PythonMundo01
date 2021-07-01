primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + 9 * razão
próximo = primeiro
if razão != 0:
    print('Os 10 primeiros termos da PA de {} com razão {} são: '.format(primeiro, razão),end='')
    while próximo != décimo + razão:
        próximo = próximo + razão
        print('{}'.format(próximo),end=' ')
        #print('. ' if próximo == décimo + razão else ', ',end='')
    opção = int(input('\nDeseja acrescentar mais termos? '
                            '\n[ 1 ] SIM'
                            '\n[ 2 ] NÃO'
                            '\nOpção: '))
    if opção == 1:
        termos = int(input('Quantos termos a mais? '))
        if termos == 0:
            print('Opção inválida! Programa Encerrado!')
        print('Continuando a PA... ', end='')
        for c in range(0, termos):
            próximo = próximo + razão
            print('{}'.format(próximo), end=' ')
        print('\nPrograma Encerrado!')
    elif opção == 2:
        print('Programa Encerrado!')
    else:
        print('Opção Inválida!')
else:
    print('A razão não pode ser 0')
