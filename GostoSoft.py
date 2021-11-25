sanduba = int(input('Quantos Sanduiche quer fazer:'))

presunto = 50.0 * 2
Queijo = 50.0
carne = 100.0

pres = presunto * sanduba
quei =  Queijo * sanduba
car = carne * sanduba
Quilos = pres + quei + car
Kg = Quilos / 1000


print('Serao nescessarios\n',pres / 1000, 'Kg de PRESUNTO\n',quei / 1000,'Kg de QUEIJO\n',car / 1000,'Kg de Carne\nTOTAL:',Kg,'Kg')