print('-=-' * 20)
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
c = 0
while c == 0:
    print('-=-' * 20)
    menu = int(input('O que você deseja fazer?'
                     '\n[ 1 ] SOMAR'
                     '\n[ 2 ] MULTIPLICAR'
                     '\n[ 3 ] MAIOR'
                     '\n[ 4 ] NOVOS NÚMEROS'
                     '\n[ 5 ] SAIR DO PROGRAMA'
                     '\nSua opção: '))
    print('-=-' * 20)
    if menu == 1:
        print('A soma entre {} e {} é igual  {}'.format(n1, n2, (n1+ n2)))
    elif menu == 2:
        print('O produto entre {} e {} é igual a {}'.format(n1, n2, (n1 * n2)))
    elif menu == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}'.format(n1, n2))
        elif n2 > n1:
            print('O número {} é maior que o número {}'.format(n2, n1))
        else:
            print('Os dois números são iguais')
    elif menu == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif menu == 5:
        print('Você saiu do programa!')
        c += 1
print('-=-' * 20)
