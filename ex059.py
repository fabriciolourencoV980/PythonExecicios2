"""
crie um programa que leia dois valores e mostre um menu na tela
"""

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

print('\n')
while True:
    print('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair')
    selecao = int(input('Digite uma opção do menu: '))
    if selecao == 1:
        soma = valor1 + valor2
        print(35 * '=')
        print(f'A soma entre {valor1} + {valor2} = {soma}')
        print(35 * '=')
    elif selecao == 2:
        multiplicacao = valor1 * valor2
        print(35 * '=')
        print(f'A multiplicação entre {valor1} x {valor2} = {multiplicacao}')
        print(35 * '=')
    elif selecao == 3:
        if valor1 > valor2:
            print(35 * '=')
            print(f'O {valor1} é maior que o {valor2}')
            print(35 * '=')
        else:
            print(35 * '=')
            print(f'O {valor2} é maior que o {valor1}')
            print(35 * '=')
    elif selecao == 4:
        print(35 * '=')
        valor1 = int(input('Digite um novo valor: '))
        valor2 = int(input('Digite outro novo valor: '))
        print(35 * '=')
    elif selecao == 5:
        print('Fim do programa!')
        break

