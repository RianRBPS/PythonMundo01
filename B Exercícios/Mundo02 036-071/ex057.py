M = 'Masculino'
F = 'Feminino'
sexo = 1
while sexo == 1:
    tipo = str(input('Qual é o sexo da pessoa? '
                     '\n[ M ] Masculino'
                     '\n[ F ] Feminino'
                     '\nSua opção: ')).upper().strip()
    if tipo == 'M':
        sexo = sexo - 1
        print('O sexo dessa pessoa é {}'.format(M))
    elif tipo == 'F':
        sexo = sexo - 1
        print('O sexo dessa pessoa é {}'.format(F))



