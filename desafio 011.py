# Desafio 011 - Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
largura = float(input('\nDigite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2

print('\nA área da parede é: {:.2f}m² e são necessários {:.2f}l para pintá-la\n'.format(area, tinta))