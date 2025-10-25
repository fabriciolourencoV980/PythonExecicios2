"""
Elabore um programa que calcule o valor a ser pago por um produto
considerando o seu preço normal e condição de pagamento
á vista dinheiro ou cheuqe 10% desconto
á vista cartão 5%
em até duas vezes no cartão preço normal
3x ou mais no cartão 20% juros
"""
print(15 * '=', 'LOJAS PREÇO BAIXO', 15 * '=')
precoNormal = int(input('Digite o valor do produto: '))
print('FORMAS DE PAGAMENTO')
formaPagamento = int(input('Digite a forma de pagamento, opção:\n[1] Dinheiro/Cheque\n[2] A vista cartão\n[3] 2x cartão\n'
'[4] 3x ou mais cartão\nDigite a opção:'))

if formaPagamento == 1:
    print(f'Valor final do produto: {precoNormal - (precoNormal * 10 / 100)}')
elif formaPagamento == 2:
    print(f'Valor final do produto: {precoNormal - (precoNormal * 5 / 100)}')
elif formaPagamento == 3:
    print(f'Valor final do produto: {precoNormal}')
elif formaPagamento == 4:
    print(f'Valor final do produto: {precoNormal + (precoNormal * 20 / 100)}')
else:
    print('[OPÇÃO INVÁLIDA]')