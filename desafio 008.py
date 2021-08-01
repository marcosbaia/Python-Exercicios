# Desafio 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
metros = float(input('\nDigite o valor em metros: '))
centimetros = metros * 100 
milimetros = metros * 1000

print('\n{} metros corresponde a {} centímetros'.format(metros, centimetros))
print('{} metros corresponde a {} milimetros \n'.format(metros, milimetros))