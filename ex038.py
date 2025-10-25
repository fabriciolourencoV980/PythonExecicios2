"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela
o primeiro valor é maior
o segundo valor é maior
Não existe valor maior, os dois são iguais
"""

primeiroValor = int(input('Digite um valor: '))
segundoValor = int(input('Digite um valor: '))

if primeiroValor > segundoValor:
    print('O primeiro valor é maior!')
elif segundoValor > primeiroValor:
    print('O segundo valor é maior!')
elif primeiroValor == segundoValor:
    print('Os valores são iguais!')