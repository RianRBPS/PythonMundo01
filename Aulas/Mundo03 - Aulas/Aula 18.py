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