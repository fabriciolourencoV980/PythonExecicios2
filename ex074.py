"""
Crie um programa que gere 5 números aleatórios e coloca em uma tupla
e mostre o maior valor sorteado e o menor valor sorteado
"""

from random import randint

n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print(f'Os valores sorteados foram: ', end=' ')

for num in n:
    print(num, end=' ')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')