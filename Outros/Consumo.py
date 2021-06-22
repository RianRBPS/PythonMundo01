# Determinar o consumo semanal de um automóvel tendo em mente
# Seu consumo dentro da cidade
# O trajeto diário
# Quantas vezes por semana será realizado o trajeto

#carro = str(input('Qual o modelo e o ano do carro? ')).strip()
consumo_gas = int(input('Quantos Km/L ele faz na gasolina? '))
kms_dia = int(input('Quantos Kms serão feitos por dia em média? '))
semana = int(input('Quantas vezes por semana o trajeto será realizado?'))
preço_gasolina = float(input('Qual o preço atual da gasolina? '))
trajeto_semanal = kms_dia * semana
consumo_semanal_gas = trajeto_semanal / consumo_gas
gastos_semanais = consumo_semanal_gas * preço_gasolina
print(gastos_semanais)