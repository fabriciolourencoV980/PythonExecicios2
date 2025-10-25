"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor
"""

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a

# Verificando quem é menor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'Menor valor: {menor}')
print(f'Maior valor: {maior}')
