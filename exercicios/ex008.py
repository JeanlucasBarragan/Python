din = float(input('Quanto dinheiro você tem? '))
dol = round(din / 5.13, 2)
print('Atualmente com R${} reais você consegue comprar USD {} dólares !' .format(din, dol))
