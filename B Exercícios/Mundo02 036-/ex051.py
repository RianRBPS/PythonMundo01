#Eu não entendo mais de PA o suficiente


primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
if razão != 0:
    for c in range(primeiro, décimo + razão, razão):
       print('{}'.format(c),end=' > ')
    print('Fim')
else:
    print('A razão não pode ser 0.')
