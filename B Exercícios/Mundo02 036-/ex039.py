#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
sexo = int(input('Determine o seu gênero: '
                 '\n[ 1 ] masculino'
                 '\n[ 2 ] feminino' 
                 '\nSua opção: '))
if sexo == 1:
    atual = date.today().year
    nascimento = int(input('Ano de nascimento: '))
    idade = atual - nascimento
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
    if idade == 18:
        print('Você tem que se alistar imediatamente.')
    elif idade < 18:
        saldo = 18 - idade
        print('Você vai precisar se alistar daqui {} anos.'.format(saldo))
    else:
        saldo = idade - 18
        print('Você precisou se alistar há {} ano(s).'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi no ano de {}'.format(ano))
else:
    print('Você não precisa se alistar')

