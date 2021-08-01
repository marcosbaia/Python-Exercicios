# Desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preco = float(input('\nQual é o preço do produto? R$ '))
desconto = (preco * 5)/100
valorFinal = preco - desconto

print('O valor do Produto é R$ {} com 5% de desconto R$ {} \nO valor a se pagar é R$ {}\n'.format(preco, desconto, valorFinal))