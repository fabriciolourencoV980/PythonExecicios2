"""
Faça um programa que leia cinco valores númericos e guarde-os em uma lista
No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
"""

valores = list()

print('-=' * 22)

for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {v}: ')))

print('-=' * 22)

for i, v in enumerate(valores):
    print(f'Posição {i} Valor digitado: {v}')

print('-=' * 22)

print(f'Você digitou os valores {valores}')

for i, v in enumerate(valores):
    if v == max(valores):
        print(f'O maior valor digitado foi {v} na posição {i}')
    if v == min(valores):
        print(f'O menor valor digitado foi {v} na posição {i}')

print('-=' * 22)
