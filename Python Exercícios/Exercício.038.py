"""
[Exercício 38]
    Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

    - O primeiro valor é maior
    - O segundo valor é maior
    - Não existe valor maior; os dois são iguais

"""

n1 = int(input('Digite seu primeiro número: '))
n2 = int(input('Digite seu segundo número: '))

if n1 > n2:
    print('O PRIMEIRO número é maior.')
elif n1 < n2:
    print('O SEGUNDO número é maior.')
else:
    print('Não existe valor maior; os dois são IGUAIS.')