print('================================')
print('       BANCO CEV')
print('================================')
cinq = vint = dez = um = 0
while True:
    valor = int(input('Que valor você quer sacar? R$'))
    if valor >= 50:
        while valor >= 50:
            cinq += 1
            valor -= 50
    if valor >= 20:
        while valor >= 20:
            vint += 1
            valor -= 20
    if valor >= 10:
        while valor >= 10:
            dez += 1
            valor -= 10
    if valor >= 1:
        while valor >= 1:
            um += 1
            valor -= 1
    break
print('================================'
      f'\n   Total de {cinq} notas de 50'
      f'\n   Total de {vint} notas de 20'
      f'\n   Total de {dez} notas de 10'
      f'\n   Total de {um} notas de 1'
      '\n================================')
