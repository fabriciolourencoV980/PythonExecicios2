"""
crie um programa que leia a idade e o sexo de varias pessoas. a cada pessoa cadastrada
o programa deverá perguntar se o usuário quer ou não continuar, no final mostre:
a quantas pessoas tem mais de 18 anos.
b quantos homens foram cadastrados.
c quantos mulheres tem menos de 20 anos.
"""

contidade = contfem = contmasc = 0

while True:
    print('-=' * 10)
    print('CADASTRAR UMA PESSOA')
    print('-=' * 10)
    idade = int(input('Idade: '))
    if idade > 18:
        contidade += 1
    sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
    if sexo == 'F' and idade < 20:
        contfem += 1
    elif sexo == 'M':
        contmasc += 1
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
    print('-' * 25)
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print('-' * 25)
    while opcao not in 'SsNn':
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        print('='* 6, 'FIM DO PROGRAMA', '=' * 6)
        break
print(f'Total de pessoas com mais de 18 anos: {contidade}')
print(f'Ao todo temos {contmasc} homens cadastrados')
print(f'E temos {contfem} mulheres com menos de 20 anos')