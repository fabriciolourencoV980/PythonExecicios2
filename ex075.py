"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla:
A) Quantas vezes aparece o 9
B) Em que posição foi digitado o valor 3
C) Quais foram os valores pares
"""
valor1 = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
          int(input('Digite o último númrto: ')))

print(f'Você digitou os valores {valor1}')
print(f'O valor 9 apareceu {valor1.count(9)} vezes')

if 3 in valor1:
    print(f'O valor 3 apareceu na {valor1.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')

print('O valores pares digitados foram ', end='')
for valor in valor1:
    if valor % 2 == 0:
        print(valor, end=' ')
