mais_18 = 0
homens = 0
mulher_20 = 0
sexo = ''
while True:
    print('-' * 30)
    print('    CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Digite a idade da pessoa: '))
    if idade > 18:
        mais_18 += 1
    print('-' * 30)
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Qual o sexo da pessoa? [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
    print('-' * 30)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{mais_18} pessoas tem mais de 18 anos, {homens} pessoas são homens e {mulher_20} mulheres tem menos de 20 anos')
