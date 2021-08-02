#Faça um algorítimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
p = float(input('Qual é o preço do produto?'))
d = p*0.95
print('O produto de preço R${:.2f} passa a valer R${:.2f} após o desconto de 5%'.format(p, d))

# d = p - (p * 5 / 100)
