"""
Faça um programa que leia um ano qualquer e diga se ele é BISSEXTO
"""

from datetime import date

ano = int(input('Digite o ano? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ANO {ano} BISSEXTO')
else:
    print(f'O ANO {ano} NÃO É BISSEXTO')