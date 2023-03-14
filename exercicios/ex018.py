num = int(input('Digite um número: '))
u = num // 1 % 10   # para pegar a unidade
d = num // 10 % 10  # para pegar a dezena
c = num // 100 % 10  # para pegar a centena
m = num // 1000 % 10  # para pegar o milhar
print('Analisando o número {}' .format(num))
print('Unidades: {}' .format(u))
print('Dezenas: {}' .format(d))
print('centena: {}' .format(c))
print('Milhar: {}' .format(m))
