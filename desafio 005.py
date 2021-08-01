# Desafio 005 - Faça um programa que um número inteiro e mostre na tela o seu sucessor e seu antecessor.
numero = int (input('\n Digite um número inteiro: '))
antecessor = numero - 1
sucessor = numero + 1

print('\n O Antecessor do número {} é {} e seu Sucessor é {} \n'.format(numero, antecessor, sucessor))