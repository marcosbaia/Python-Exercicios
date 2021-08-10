# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um Triângulo Retângulo. Calcule e mostre o comprimento da hipotenusa. 
import math
cateto_oposto = float(input('\nDigite o comprimento do Cateto Oposto: '))
cateto_adjacente = float(input('Digite o comprimento do Cateto Adjacente: '))

#Teorema de Pitagoras
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print('\nA hipotenusa vai medir {:.2f}\n'.format(hipotenusa))