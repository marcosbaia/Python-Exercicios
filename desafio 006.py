# Desafio 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
numero = int (input('\nDigite um número inteiro: '))
dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero * numero

print('\nO Dobro de {} é {}'.format(numero, dobro))
print('O Triplo de {} é {}'.format(numero, triplo))
print('A Raiz Quadrada de {} é {} \n'.format(numero, raizQuadrada))