"""
Faça um programa que leia o peso de cinco pessoas, no final mostre qual foi o maior e menor peso lido.
"""

maior = 0
menor = 0

for p in range (1,6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}kg.')
print(f'O menor peso lido foi {menor}kg.')