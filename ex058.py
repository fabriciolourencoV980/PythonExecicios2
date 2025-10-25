"""
Melhore o jogo do desafio 028
onde o comutador vai pensar em um número entre 0 e 10 o jogador vai tentar advinhar até acertar
final quantos palpites forem necessários para acertar
"""

from random import randint

computador = randint(0, 10)
n = int(input('Advinhe o número sorteado: '))
acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez!')
        elif jogador > computador:
            print('Menos...Tente mais uma vez!')
print(f'Acertou com {palpite} palpites [PARABÉNS]!')