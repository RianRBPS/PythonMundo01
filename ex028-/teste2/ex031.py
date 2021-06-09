#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prester a realizar uma viagem de {}Km.'.format(distancia))

if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45

# passagem = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print('O valor da passagem vai ser R${:.2f}'.format(passagem))
