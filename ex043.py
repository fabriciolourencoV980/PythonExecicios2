"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa e calcule seu IMC
e mostre seu status de acordo com a tabela:
18.5 abaixo do peso
entre 18.5 e 25 ideal
25 até 30 sobrepeso
acima de 40 obesidade morbida
"""

peso = float(input("Digite o peso em Kg: "))
altura = float(input("Digite sua altura em m: "))
imc = peso / (altura**2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 25 and imc >= 18.5:
    print("Peso ideal")
elif imc <= 30 and imc >= 25:
    print("Sobrepeso")
elif imc <= 40 and imc >= 30:
    print("Obesidade")
else:
    print("Obesidade morbida")