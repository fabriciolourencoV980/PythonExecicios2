"""
Crie um programa que faça o computador jogar jokenpô com você
"""

from random import randint
from time import sleep

print('Qual a sua jogada? ')
opcao = int(input('[0] Pedra \n[1] Papel \n[2] Tesoura\nDigite:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
escolha = randint(0, 2)

print(20 * '-=')
if opcao == 0:
    print('Você escolheu Pedra!')
elif opcao == 1:
    print('Você escolheu Papel!')
elif opcao == 2:
    print('Você escolheu Tesoura!')

if escolha == 0:
    print('A máquina escolheu Pedra!')
elif escolha == 1:
    print('A máquina escolheu Papel!')
elif escolha == 2:
    print('A máquina escolheu Tesoura!')
print(20 * '-=')

if opcao == 0 and escolha == 0 or opcao == 1 and escolha == 1 or opcao == 2 and escolha == 2:
    print('[EMPATE]')
elif opcao == 0 and escolha == 1 or opcao == 1 and escolha == 2 or opcao == 2 and escolha == 0:
    print('[A MÁQUINA VENCEU]')
elif opcao == 0 and escolha == 2 or opcao == 1 and escolha == 0 or opcao == 2 and escolha == 1:
    print('[VOCÊ VENCEU]')
else:
    print('[OPÇÃO INVÁLIDA]')
