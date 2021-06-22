nome = str(input('Qual é o seu nome? '))
if nome == 'Rian':
    print('Que nome lindo')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome mulher!')
else:
    print('Que nome normal')
print('Tenha um bom dia {}!'.format(nome))
