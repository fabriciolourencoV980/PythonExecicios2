"""
Crie um programa que simule o funcionamento de um caixa eletronico. no inicio pergunte ao usuário
qual será o valor a ser sacado, e o programa vai informar quantas cedulas de cada valor serão entregues
cadulas 50 20 10 1
"""


#[ERRO] - Para correção **

print('=' * 30)
print('{:*^30}'.format(' BANCO CEV '))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print(f'Total de {totalced} cédulas de R${total}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if totalced == 0:
            break