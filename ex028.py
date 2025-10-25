"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deve escrever na tela se o usuário venceu ou perdeu"""

from random import randint

aleatorio = randint(0,5)
n = int(input('Advinhe o número sorteado: '))

if aleatorio == n:
    print(f'Parabens você acertou! O número sorteado foi de {aleatorio}\nE o numero que você digitou foi: {n}')
else:
    print(f'Infelizmente não foi dessa vez o número sorteado foi: {aleatorio}\nE o número digitou foi: {n}')

print('[FIM DO JOGO]')