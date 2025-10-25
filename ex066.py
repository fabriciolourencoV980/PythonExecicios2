"""
Crie um programa que leia varios números inteiros, o programa só vai parar quando digitar o valor
999. No final mostre quantos números foram digitados e qual foi a soma entre eles
"""

cont = soma = 0

while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} valores foi {soma}!')