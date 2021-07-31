# Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
print('')
algo = input('Digite algo: ')

print('................................................................')
print('O valor digitado é do tipo primitivo?        >> ', type(algo))
print('O valor digitado só contém espaço?           >> ', algo.isspace())
print('O valor digitado é um número?                >> ', algo.isnumeric())
print('O valor digitado pertence ao alfabeto?       >> ', algo.isalpha())
print('O valor digitado esta em letras maiusculas?  >> ', algo.isupper())
print('O valor digitado esta em letras minusculas?  >> ', algo.islower())
print('O valor digitado esta capitalizado?          >> ', algo.istitle())
print('................................................................')