valorDeADD = float(input('Valor de aquisição do produto:'))

if valorDeADD < 50.00:
    valor = valorDeADD * 1.45
    print('Novo valor do produto: R$', valor)
elif valorDeADD >= 50.00:
    valor = valorDeADD * 1.30
    print('Novo valor do produto: R$', valor)