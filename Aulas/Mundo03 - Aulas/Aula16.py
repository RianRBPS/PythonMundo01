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
print(sorted(lanche2)) #Em ordem

for comida in lanche: #Não tem como mostrar posição
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche2)):
    print(f'Eu vou comer {lanche2[cont]} na posição {cont}')

for pos, comida in enumerate(lanche2): #Posição enumerada
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #Ordem dos fatores altera o resultado
d = b + a
print(len(c))
print(d)
print(c)
print(c.count(9)) # Quantas vezes o 9 apareceu
print(c.index(8)) # Em que posição está o 8
print(c.index(5, 1))# Primeiro 5 a partir da posição 1

pessoa = ('Gustavo', 39, 'M', 99.88) # Em java não pode misturar tipos diferentes nas tuplas
del(pessoa) #Deleta a tupla
