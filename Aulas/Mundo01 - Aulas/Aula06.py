#int = Números inteiros ( 7 -4 0 9857)
#float = Números reais (4.5 / 0.0076 / -15.223 / 7.0 / π )
#bool = True False (T e F maísculos)
#str = 'Olá' / '7.5'  / '' (string vazia)

n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número:'))
s = n1 + n2
print('A soma é:', s)

print('A soma vale {}'.format(s))

#O nome dessa pora {} é chave

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
#print('A soma entre', n1,'e', n2, 'vale', s)
print('A soma entre {} e {} vale {}'.format(n1,n2,s))
#print('A soma entre {1} e {2} vale {3}'.format(n1,n2,s)

n = input('Digite algo:')
#print(n.isnumeric())
#print(n.isalpha())
print(n.isupper())
