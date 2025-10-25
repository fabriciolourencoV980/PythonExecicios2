"""
Pragrama que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade.
"""

from datetime import date

idade = int(input('Digite o seu ano de nascimento: '))
data = date.today()
anoAtual = data.year
categoria = anoAtual - idade
print(f'O atleta tem {categoria} anos.')

if categoria <= 9:
    print('Categoria: [MIRIM]')
elif categoria <= 14 and categoria >= 10:
    print('Categoria: [INFANTIL]')
elif categoria <= 19 and categoria >= 15:
    print('Categoria: [JUNIOR]')
elif categoria == 20:
    print('Categoria: [SENIOR]')
else:
    print('Categoria: [MASTER]')

