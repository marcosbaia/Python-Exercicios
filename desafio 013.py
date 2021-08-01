# Desafio 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. 
salario = float(input('\nDigite o valor do salário do funcionário: R$ '))
aumento = (salario * 15)/100
novoSalario = salario + aumento
print('O Novo salário do funcionário é R$ {:.2f}\n'.format(novoSalario))