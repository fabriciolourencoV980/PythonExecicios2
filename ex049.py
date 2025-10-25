"""
Desafio tabuada de um número que o usuário escolher
"""

n = int(input('Digite um número para ver sua tabuada: '))

for i in range(0, 11):
    print(f'{n} x {i} = {n * i}')