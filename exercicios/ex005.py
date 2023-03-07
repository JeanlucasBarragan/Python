print('Olá seja-bem Vindo, vamos calcular sua média?')
aluno = input('Digite seu nome: ')
nota1 = float(input('Qual sua nota no 1º semestre?'))
nota2 = float(input('Qual sua nota no 2º semestre?'))
media = (nota1 + nota2) / 2
if media < 5:
    print(aluno)
    print('Média final: ', float(media))
    print('REPROVADO(a) !!')
else:
    print(aluno)
    print('Média final: ', float(media))
    print('APROVADO(a), PARABÉNS')
