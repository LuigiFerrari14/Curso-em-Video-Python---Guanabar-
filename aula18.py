teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)


galera = [['joao', 19],['maria', 20]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] > 20:
        print(f' {p[0]} tem {p[1]} anos! ')


galera = list()
dados = list()
total = cont = maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    cont+=1
    if cont == 1:
        maior = dados[1]
        menor = dados[1]
    if cont > 1:
        if dados[1] > maior:
            maior = dados[1]
        if menor > dados[1]:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    total+=1

    resp = input('Quer continuar? [S/N]: '.upper())
    while resp.upper() not in 'SN':
        resp = input('Digite apenas [S/N]: ')
    if resp.upper() == 'S':
        print('Continuando...')
    else:
        print('-'*50)
        break
print('Ao todo, você cadastrou {} pessoas'.format(total))
print(f'O maior peso é {maior}kg.', end='')
for p in galera:
    if p[1] == maior:
        pesado = ''
        pesado = p[0]
print(pesado)
print(f'o menor peso é: {menor}kg.', end='')
for p in galera:
    if p[1] == menor:
        leve = ''
        leve = p[0]
print(leve)



listageral = [[], []]
valor = 0

for t in range(0, 7):
    valor = (int(input('Digite um número: ')))
    if valor % 2 == 0:
        listageral[0].append(valor)
    else:
        listageral[1].append(valor)

listageral[0].sort()
listageral[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {listageral[0]}')
print(f'Os valores impares digitados foram: {listageral[1]}')



maior = 0
somacolona = 0
somapar = 0
matrix = [[0,0,0],[0,0,0],[0,0,0]]
for l1 in range(0,3):
    for c in range(0, 3):
        numero = int(input(f'Digite um valor para [{l1}, {c}]: '))
        if numero % 2 == 0:
            somapar+=numero
        if c == 2:
            somacolona+=numero
        if l1 == 1 and c == 0:
            maior = numero
        elif l1 == 1:
            if numero > maior:
                maior = numero

        matrix[l1][c] = numero
print('-=' * 30)
for l1 in range(0,3):
    for c in range(0, 3):
        print(f'[{matrix[l1][c]:^5}]',end='')
    print()
print(f'A soma dos números pares é de: {somapar}')
print(f'A soma da terceira coluna é de: {somacolona}')
print(f'O maior número da segunda linha é de: {maior}')


import random
import time
print('-'*30)
print('          Mega Sena          ')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
lista = list()
jogos = list()
while tot <= quant:
    cont = 0
    while True:
        num = random.randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print(f'-=' * 3,f' Sorteando {quant} jogos ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1} = {l}')
    time.sleep(1.5)
print(f'-=' * 4,' Boa Sorte!! ', '-=' * 4)








