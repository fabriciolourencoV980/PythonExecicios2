"""
Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$ 7,00 por cada Km acima do limite.
"""

velocidade = float(input('Qual a velocidade atual do carro?'))

if velocidade > 80:
    print('[MULTADO] Excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R$ {multa:.2f}')