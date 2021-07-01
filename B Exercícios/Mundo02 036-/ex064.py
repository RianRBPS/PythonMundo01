n = 1
soma = 0
acumulador = 0
while n != 999: # FLAG
    n = int(input('Digite um valor: '))
    acumulador += 1
    soma = soma + n
tentativas = (acumulador - 1)
soma_final = soma - 999
print('Foram digitados {} números antes de 999, a soma de todos os números digitados antes de 999 é igual a {}.'.format(tentativas, soma_final))
