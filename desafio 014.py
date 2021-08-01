# Desafio 014 - Escreva um programa que converta uma temperatura digitada em celsius para Fahrenheit.
celsius = float(input('\nDigite a temperatura em Celsius: '))
fahrenheit = (celsius * 1.8) + 32

print('\nA temperatura {}ºC em Celsius corresponde a {}ºF em Fahrenheit.\n'.format(celsius, fahrenheit))

