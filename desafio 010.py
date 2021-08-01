# Desafio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$3,27
dinheiro = float(input('\nDigite quanto você tem? R$ '))
dolar = dinheiro / 3.27
print('\nCom R$ {} é possível comprar US$ {:.2f} \n'.format(dinheiro, dolar))