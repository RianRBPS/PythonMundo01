# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date
ano = date.today().year
nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = ano - nascimento
if idade <= 9:
    print('O atleta nasceu no ano {}.'
          '\nSua categoria é MIRIM.'.format(nascimento))
elif 9 < idade <= 14:
    print('O atleta nasceu no ano {}.'
          '\nSua categoria é INFANTIL.'.format(nascimento))
elif 14 < idade <= 19:
    print('O atleta nasceu no ano {}.'
          '\nSua categoria é JÚNIOR.'.format(nascimento))
elif 19 < idade <= 25:
    print('O atleta nasceu no ano {}.'
          '\nSua categoria é SÊNIOR.'.format(nascimento))
else:
    print('O atleta nasceu no ano {}.'
          '\nSua categoria é MASTER.'.format(nascimento))
print('O atleta tem {} anos'.format(idade))
