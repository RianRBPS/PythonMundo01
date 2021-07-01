n = 1
soma = 0
divisor = 0
acumulador = 0
maior = n
while n != 0: # FLAG
    n = int(input('Digite um valor: '))
    acumulador += 1
    opção = int(input('Deseja continuar digitando valores? '
                      '\n[ 1 ] SIM'
                      '\n[ 2 ] NÃO'
                      '\nSua opção: '))
    divisor += 1
    soma = soma + n
    if opção == 1:
        n = 1
    elif opção == 2:
        n = 0
média = soma / divisor
print('A média entre todos os valores digitados é {:.1f}.'.format(média))
print(acumulador)
