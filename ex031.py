"""
Desenvolva um programa que pergunte a distancia de uma viagem em Km.
Calcule o preço da passagem, cobrando 0,50 por km para viagens de até 200km
e 0,45 para viagens mais longas.
"""

distancia = float(input('Digite a distancia da sua viagem: '))
print(f'Você está prestes de começar uma viagem de {distancia} km.')

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'E o preço da sua passagem será de R${preco:.2f}')