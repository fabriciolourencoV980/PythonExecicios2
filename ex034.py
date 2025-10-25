"""
Programa que pergunte o salario e calcule o aumento
Salarios maiores que 1.250 aumento de 10%
salarios menores que 1.250 aumento de 15%
"""

salario = float(input('Qual o salario do funcionario? R$'))

if salario >= 1250:
    novo = salario + (salario * 10 / 100)
else:
    novo = salario + (salario * 15/100)

print(f'Quem ganhava R${salario} passa a ganhar R${novo}')

