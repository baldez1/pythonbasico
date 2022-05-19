real = float(input('Quanto dinheiro você tem na sua carteira? R$'))
dolar = real / 5.13
print('Com R${:.2f} você pode comprar US${:.2f}' .format(real, dolar))