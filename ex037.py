"""
Escreva um número inteiro qualquer e peça para o usuário escolher a base de conversão
1 Binario
2 Octal
3 Hexadecimal
"""

numero = int(input('Digite um número: '))
conversao = int(input('Digite a base de conversao:\nSendo:\n[1] Binário\n[2] Octal\n[3] Hexadecimal\nDigite:'))

if conversao == 1:
    print(f'O número convertido para binario é {bin(numero)[2:]}')
elif conversao == 2:
    print(f'O número convertido para octal é {oct(numero)[2:]}')
elif conversao == 3:
    print(f'O número convertido para hexadecimal é {hex(numero)[2:]}')
else:
    print('[OPÇÃO INVÁLIDA]')