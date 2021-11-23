'''Atividade Qual combustivel mais viavel'''
KMA = int(input('Quantos KM faz com um litro de alcool:'))
KMG = int(input('Quantos KM faz com um litro de gasolina:'))
precoA = float(input('Quanto custa o litro alcool:'))
precoG = float(input('Quantos custa a litro gasolina:'))
kmRodado = int(input('Quantos KM sera percorrido:'))

KMRA =  precoA * KMA / kmRodado
KMRG =  precoG * KMG / kmRodado

if KMRA < KMRG:
    print('Alcool esta compensando mais!!')
else:
    print('Gasolina esta compensando mais!!')
