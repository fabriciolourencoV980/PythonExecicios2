"""
Faça um programa que leia um número qualquer e mostre o seu fatorial
"""

# from math import factorial
#
# n = int(input('Digite um número para calcular o seu fatorial: '))
# f = factorial(n)
# print(f'O Fatorial de {n} é igual a {f}')

# n = int(input('Digite um número: '))
# c = n
# f = 1
# print(f'Calculando {n}! = ', end='')
#
# while c > 0:
#     print(f'{c}', end='')
#     print(' x ' if c > 1 else ' = ', end='')
#     f *= c
#     c -= 1
# print(f)

n = int(input('Digite um número: '))
c = n
f = 1

for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f)