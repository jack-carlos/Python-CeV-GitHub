"""
[Exercício 33]
    Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um último número: '))
l = [n1, n2, n3]
l.sort()
print(f'O maior número é {l[2]} e o menor é {l[0]}')

# O método .sort() ordena os números da lista em ordem crescente.