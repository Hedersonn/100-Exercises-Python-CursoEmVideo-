#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 999

for i in range(1, 6):
    peso = float(input(f'{i}º peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('-' * 40)
print(f'O maior peso é {maior:.1f}kg')
print(f'O menor peso é {menor:.1f}kg')
print('-' * 40)