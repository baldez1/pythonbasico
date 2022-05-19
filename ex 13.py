salário = float(input('Qual é o valor do seu salário? R$'))
novo = salário + (salário + 15 / 100)
print('O seu sálario que custava R${:.2f}, com 15% de aumento irá receber R${:.2f}'.format(salário, novo))