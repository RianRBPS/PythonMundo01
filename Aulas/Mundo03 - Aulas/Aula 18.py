dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0]) #Pedro
print(dados[1]) #25

pessoas = list()
pessoas.append(dados[:]) #Cópia dos dados
# [['Pedro', 25]]  Elemento 0
# [['Maria', 19]]  Elemento 1
# [['João', 32]]   Elemento 2
print(pessoas)

# Listas compostas (Listas dentro de listas)
pessoas2 = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas2[0][0]) # Pedro(Elemento 0 da lista composta 0)
print(pessoas2[1][1]) # 19   (Elemento 1 da lista composta 1)
print(pessoas2[2][0]) # José (Elemento 0 da lista 2)
print(pessoas2[1])    # ['Maria', 19]

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera2:
    print(p)
    #print(p[0]) só o nome
    print(f'{p[0]} tem {p[1]} anos de idade')
print(galera2[2][1])

galera3 = list()
dado = list()
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade:  ')))
    galera3.append(dado[:])
    dado.clear()

totmai = totmen = 0
for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiorese {totmen} menores de idade')