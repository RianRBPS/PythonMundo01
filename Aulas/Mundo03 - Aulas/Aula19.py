# Tuplas ()
# Listas []
# Dicionários {}

# dados = dict()
# dados = {            }


dados = {'nome':'Pedro', 'idade': 25}
print(dados['nome'])  # Pedro
print(dados['idade']) # 25

dados['Sexo'] = 'M'

del(dados['idade'])

filme = {'título': 'Star wars',
         'ano': 1957,
         'diretor': 'George Lucas'
}

print(filme.values()) # Valores
print(filme.keys())   # Chaves
print(filme.items())  # Valores e Chaves

#for k, v in filme.items():
    #print(f'O {k} é {v}')

pessoas = {'nome2': 'Gustavo',
           'sexo': 'M',
           'idade': 22}

pessoas['nome2'] = 'Leando'
pessoas['peso'] = 98.5
del  pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado = {'uf':'Rio de Janeiro', 'silgra': 'RJ'}
estado2 = {'uf':'São Paulo', 'sigla': 'SP'}
brasil.append(estado)
brasil.append(estado2)

print(brasil[0]) #RJ

estado3 = dict()
brasil = list()
for c in range(0, 3):
    estado3['uf'] = str(input('Unidade Federativa: '))
    estado3['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado3.copy())
    #brasil.append(estado3)     Não da certo
    #brasil.append(estado3[:])  Não da certo
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
  
