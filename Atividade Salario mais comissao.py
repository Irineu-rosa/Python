'''Atividade Salario mais comissao'''
salario = int(input('Digite valor do salario:'))
venda = int(input('Digite o valor de suas vendas:'))
if venda > 20000:
    cont = salario * 0.05
    slcm = salario + cont
    print('Salario mais comissão R$', slcm)
elif venda <= 20000:
    cont = salario * 0.04
    slcm = salario + cont
    print('Salario mais comissão R$',slcm)