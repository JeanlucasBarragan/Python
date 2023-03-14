nome = str(input('Digite seu nome completo: ')).strip()  # .strip() elimina os espaços do inicio e final da str
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}' .format(nome.upper()))    # .upper() transforma em maiúsculas a str
print('Seu nome em minúsculas é {}' .format(nome.lower()))    # .lower transforma em minúsculas a str
print('Seu nome tem ao todo {} letras.' .format(len(nome) - nome.count(' '))) #.count elimina os espaços no meio da str
#print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))   .find() manda encontrar o primeiro espaço

separa = nome.split()  #.split() pega os dados digitados e cria uma lista
print('Seu primeiro nome é {} e ele tem  {} letras.' .format(separa[0], len(separa[0])))
