lanche = ['arroz','feijao','carne']
print(lanche)
lanche[2] = 'batata'
print(lanche)

#adiciona mais um no final da lista
lanche.append('Purê')
print(lanche)

#adiciona mais um no lugar que voce deseja
lanche.insert(0,'Guarana')
print(lanche)

#2 metodos para apagar um item da lista
del lanche[4]
print(lanche)

#lanche.pop() caso deixar vazio, irá eliminar o ultimo item
lanche.pop(3)
print(lanche)

lanche.remove('Guarana')
print(lanche)

#sort() Valores em ordem crescente // sort(reverse=True) Decrescente


valores = list()
valores.append(1)
valores.append(3)
valores.append(5)

for c, v in enumerate(valores):
    print(f'Na posicão numero {c} encontrei o número {v}')
print('Cheguei no fim da lista!')


#fazer uma copia da lista
a = [2,5,7,9]
b = a #isso não é copia, isso iguala, caso mude um valor de B irá alterar o Valor de A
#para fazer copia corretamente use
b = a[:]




#DESAFIOS

valores = list()
menor = 0
maior = 0
maiorposicao = 0
menorposicao = 0
cont = 0
for l in range(0,5):
    valores.append(int(input('Digite o valor da Posição número {}: '.format(l))))
    cont+=1
    if cont == 1:
        menor = valores[l]
        maior = valores[l]
    if cont > 1:
        if menor > valores[l]:
            menor = valores[l]
        if valores[l] > maior:
            maior = valores[l]
print(f'O maior é: {maior} e está na posição', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(i)

print(f'O menor é: {menor} e está na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(i)


lista = list()
contador = 0
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Número já foi cadastrado! Tente outro')

    resposta = input('Deseja continuar? [S/N]: '.upper())
    while resposta.upper() not in 'SN':
        input('Responda com apenas [S/N]: '.upper())
    if resposta.upper() == 'S':
        print('Continuando...')
    elif resposta.upper() == 'N':
        break
print(sorted(lista))
print('Fim...')


ordem = 0

lista = list()
for contador in range(0,5):
    numero = int(input('Digite um número: '))
    if contador == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <=lista[pos]:
                lista.insert(pos, numero)
                break
            pos+=1

print(lista)

lista = list()

temcinco = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 5:
        temcinco = 1
    lista.append(numero)
    resposta = input('Deseja continuar? [S/N]: '.upper())
    while resposta.upper() not in 'SN':
        resposta = input('Responda somente com [S/N]: '.upper())
    if resposta.upper() == 'S':
        print('Continuando...')
    else:
        print('Finalizando...')
        break
print(f'Foram digitados {len(lista)} numeros')
lista.sort(reverse=True)
print(f'A ordem dos valores em ordem decrescente é {lista}')
if temcinco == 1:
    print('Tem o valor 5!')
else:
    print('Não tem o valor 5!')



lista = list()
pares = list()
impares = list()

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    resp = input('Deseja continuar [S/N]? '.upper())
    while resp.upper() not in 'SN':
        resp = input('Digite apenas [S/N]: '.upper())
    if resp.upper() == 'S':
        print('Continuando...')
    elif resp.upper() == 'N':
        print('Finalizando...')
        break
for cont in range(0,len(lista)):
    if lista[cont] % 2 == 0:
        pares.append(lista[cont])
    else:
        impares.append(lista[cont])

print('Sua lista é: {}'.format(lista))
print('Números pares {}'.format(pares))
print('Números impares {}'.format(impares))







