#Tuplas são imutáveis

#lanche = (Tupla) [Lista] {Dicionário}

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[0])
print(lanche[3])
print(lanche[-1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])

print(len(lanche))
lanche2 = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche2))
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for cont in range(0, len(lanche2)):
    print(lanche[cont])
    print(f'Eu vou comer {lanche2[cont]} na posição {cont}')

for pos, comida in enumerate(lanche2):
    print(f'Eu vou comer {lanche2[pos]} na posição {cont}')