nome = input('Digite seu nome Completo: ')

print('O nome com todas as letras maiusculas: {}'.format(nome.upper()))

print('O nome com todos minusculos: {}'.format(nome.lower()))
nome = nome.split()
print('Quantas letras ao todo sem contar os espaços: {}'.format(len("".join(nome))))
print('Quantas letras tem o primeiro nome: {}'.format(len(nome[1])))

numero = int(input('Digite em numero entre 0 e 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}'.format(m, c, d, u))

cidade = input('Digite o nome de sua cidade: ')
cidade = cidade.split()
cidade = (cidade[0])
print('sao' in cidade)
if ('sao' in cidade):
    print('Tem')
else:
    print('Não tem')

silva = input('Digite seu nome: ')
if('Silva' in silva):
    print('Tem Silva no nome!')
else:
    print('Não tem Silva no nome!')

frase = input('Escreva uma frase: ').lower()

print('A letra A aparece: {} vezes!'.format(frase.count('a')))
print('Aparece primeira na posição: {}'.format(frase.find('a')))
print('Aparece a ultima vez na posição {}'.format(frase.rfind('a')))

nome = input('Digite seu nome: ')
nome = nome.split()
print('O primeiro nome é: {} e o ultimo nome é {}'.format(nome[0], nome[len(nome)-1]))


