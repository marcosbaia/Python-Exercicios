# Desafio 016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua posição inteira.
#               Ex.: Digite um número: 6.127
#               O número 6.127 tem a parte inteira 6.
import math
numero = float(input('\nDigite um número: '))
print('O número {} tem a parte inteira {} \n'.format(numero, math.trunc(numero)))

