#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

mulheres_vinte = 0
total_idade = 0
maioridade_homem = 0
nomevelho = ''

for c in range(1, 5):
    nome = str(input('Qual é o nome da {}ª pessoa? '.format(c)))
    idade = int(input('Qual é a idade da {}ª pessoa? '.format(c)))
    if c != 0:
        total_idade = idade + total_idade
    sexo = int(input('A {}ª pessoa é:'
               '\n[ 1 ] Homem'
               '\n[ 2 ] Mulher'
               '\n[ 3 ] Outro'
               '\nOpção: '.format(c)))
    if sexo == 1 and c == 1:
        maioridade_homem = idade
        nomevelho = nome
    if sexo == 1 and idade > maioridade_homem:
        maioridade_homem = idade
        nomevelho = nome
    elif sexo == 2:
        if idade < 20:
            mulheres_vinte += 1

média_idade = total_idade / 4
print('A média de idade do grupo é de {} anos.'.format(média_idade))
print('O número de mulheres com menos de 20 anos é de {}.'.format(mulheres_vinte))
print('A idade do homem mais velho é {}, o seu nome é {}.'.format(maioridade_homem, nomevelho))
