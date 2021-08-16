# Desafio 015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Quantos dias o carro foi Alugado: '))
km = float(input('Quantos km o carro Percorreu:'))

pagar = (dias * 60) + (km * 0.15)
print('O valor a ser pago pelo Aluguel do carro é R${:.2f}'.format(pagar))

