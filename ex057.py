"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado peça a dogotação até ter um valor correto
"""

sexo = str(input('Digite seu sexo: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]


if sexo == 'M':
    print('Sexo masculino registrado com sucesso!')
elif sexo == 'F':
    print('Sexo feminino registrado com sucesso!')
