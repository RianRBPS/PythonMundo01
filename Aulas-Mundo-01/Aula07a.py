#nome = input('Qual é o seu nome?')
#print('Prazer em te conhcer {:=^20}'.format(nome))

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {},  o produto vale {} e \n a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))

#{:.3f} Determinar o valor de casas decimais
#.format(x, y), end=' ') Não quebrar a linha
# \n Quebrar a linha
