somaidade = 0
média_idade = 0
maioridadedehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('-----{}ªPESSOA-----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'M':
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadedehomem:
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
média_idade = somaidade / 4
print('A média de idades dos membros do grupo é de {} anos.'.format(média_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadedehomem, nomevelho))
print('Ao todos são {} mulheres com menos de 20 anos.'.format(totmulher20))

