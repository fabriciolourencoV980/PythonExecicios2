"""
Crie um programa que leia o ano de nascimento de sete pessoas, e no final mostre quantas
pessoas ainda não atingiram a maioridade e quantas ja são maiores
"""
from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range (1, 8):
    nasc = int(input(f'Digite o ano em que {pess}ª pessoa nasceu? '))
    idade = atual - nasc

    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print(f'Ao todo tivemos {totmaior} pessoas maior de idade!')
print(f'Ao todo tivemos {totmenor} pessoas menor de idade!')