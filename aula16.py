lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for c in lanche:
    print(c)


print(lanche[1:3])


for cont in range(0, len(lanche)):
    print(lanche[cont])

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} em {pos} lugar')

#Ordem Alfabetica!

print(sorted(lanche))


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
#count para contar quantas vezes o (X) aparece
print(c.count(5))

#index mostra a posição que se encontra o (X)
# o segundo valor dps da , é o start, vai começar a contar depois da posicao X
print(c.index(5, 1))



contagem = (0,1,2,3,4,5)
escrito = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco')
numero = int(input('Digite um número entre 0 e 5: '))
while numero > 5 or numero < 0:
    numero = int(input('Tente novamente! Digite um número entre 0 e 5: '))
print(f'Você digitou o numero {numero} que se escreve assim: {escrito[numero]}')



clubes = ('Athletico Paranaense',
'Gremio',
'Avaí',
'Bahia',
'Botafogo',
'Ceará',
'Chapecoense',
'Corinthian',
'Santos',
'CSA',
'Flamengo',
'Fluminense',
'Fortaleza',
'Goiás',
'Atlético Mineiro',
'Internacional',
'Palmeiras',
'Cruzeiro',
'São Paulo',
'Vasco da Gama')
contagem = 1
print('Os 5 primeiros times são: ')

for cincoprimeiros in clubes[0:5]:
    print(f' {contagem}-- {cincoprimeiros}')
    contagem +=1


contagemmenor = 17
print('Os 4 ultimos times são: ')

for quatroultimos in clubes[16:]:
    print(f' {contagemmenor}-- {quatroultimos}')
    contagemmenor += 1


print('Times em Ordem alfabetica:')
print(f'--> {sorted(clubes)}')
print(f'A chapeconse se encontra na posição número: {clubes.index("Chapecoense")+1}')


import random
num1 = random.randrange(0,10)
num2 = random.randrange(0,10)
num3 = random.randrange(0,10)
num4 = random.randrange(0,10)
num5 = random.randrange(0,10)
lista = (num1, num2, num3, num4, num5)
print('numeros gerados: {}'.format(lista))
print('O maior numero foi {} e o menor foi {}'.format(max(lista) ,min(lista)))


num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
num3 = int(input('Digite um valor: '))
num4 = int(input('Digite um valor: '))
lista = (num1, num2, num3, num4)

if lista[1:5] != '3':
    print('Você não digitou o valor 3!')
else:
    print('O primeiro valor 3 está na posição: {} '.format(lista.index(3) + 1))

print('Voce digitou os numeros {}'.format(lista))
print('O Valor 9 apareceu {} vezes'.format(lista.count(9)))


cont = 0
pares = 0
print('Os valores pares foram: ', end='')
for cont in range(0,4):
    if lista[cont] % 2 == 0:
        print(lista[cont])
        pares+=1
        cont+=1

print('No total foram {} números pares'.format(pares))



produtos = ('camisa', 10.25, 'Calça', 5, 'Meia', 2)
cont = 0

print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' * 40)
for cont in range(0,len(produtos)):
    if cont % 2 == 0:
        print(f'{produtos[cont]:.<30}',end='')
    else:
        print(f'R${produtos[cont]:>7.2f}')

print('-' * 40)


