"""
Crie um programa que leia varios números inteiros pelo teclado, o programa só vai parar
quando o usuário digitar 999, que é a condição de parada, no final mostre quantos números foram
digitados e qual a soma entre eles
"""

num = cont = soma = 0
num = int(input('Digite um número [999] para parar: '))

while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999] para parar: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}!')