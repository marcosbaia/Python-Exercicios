# Desafio 014 - Escreva um programa que converta uma temperatura digitada em celsius para Fahrenheit.
celsius = float(input('\nDigite a temperatura em Celsius: '))
fahrenheit = ((9 * celsius)/ 5) + 32 
 
print ('A temperatura {}°C em Celsius corresponde a {}°F em Fahrenheit\n'.format(celsius, fahrenheit))
