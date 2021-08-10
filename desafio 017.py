# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um Triângulo Retângulo. Calcule e mostre o comprimento da hipotenusa. 
cateto_oposto = float(input('\nDigite o comprimento do Cateto Oposto: '))
cateto_adjacente = float(input('Digite o comprimento do Cateto Adjacente: '))

#Teorema de Pitagoras
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print('\nA hipotenusa vai medir {:.2f}\n'.format(hipotenusa))