"""
Escreva um programa para aprovar emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o salario do comprador em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo será
negado.
"""

valorCasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salario do comprador: R$'))
anos = int(input('Digite em quantos anos de financiamento? '))
valorPrestacao = valorCasa / (anos * 12)
porcentagem = salario * 30 / 100
print(f'Para pagar uma casa de {valorCasa:.2f} em {anos} anos, a prestação será de R${valorPrestacao:.2f}.')

if valorPrestacao > porcentagem:
    print('[EMPRESTIMO NEGADO]')
else:
    print('[EMPRESTIMO APROVADO]')

