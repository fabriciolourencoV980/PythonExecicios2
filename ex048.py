"""
Faça um programa que calcule a soma entre todos os números impares que são multiplos de 3
e que se encontram no intervalo entre 1 ate 500
"""

soma = 0 #Acumulador
cont = 0 #Contador

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de todos os {cont} valores solicitados é: {soma}')