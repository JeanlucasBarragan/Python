altura = float(input('Qual altura de sua parede? '))
larg = float(input('Qual a largura de sua parede? '))
area = altura * larg
tinta = round(area / 2, 2)
print('Será nescessário {} litros de tinta para pintar sua parede !' .format(tinta))
