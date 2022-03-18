contador = 0
soma = 0
while True:
    n = int(input('Digite um Número: '))
    if n == 999:
        break
    else:
        contador += 1
        soma+=n
print(f'{contador} números foram digitados, e a soma foi de {soma}')




while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break
    else:
        for c in range(0,10):
            mult = numero * c
            print(f'{numero} * {c} = {mult}')
print('Fim!')





#JOGO DO PAR OU IMPAR
import random
vitorias = int(0)
while True:
    numero = int(input('Digite um valor: '))
    parouimpar = input('Par ou Impar? [I/P] '.upper())
    pc = random.randrange(0,10)
    resultado = numero + pc
    print('O computador escolheu o numero {} e a soma deu: {}'.format(pc,resultado))
    if parouimpar.upper() == 'I':
        if resultado % 2 == 0:
            print('Você perdeu! Ganhou o total de {} vitorias'.format(vitorias))
            break
        else:
            vitorias += 1
            print('Você Venceu! Continue jogando.')
    elif parouimpar.upper() == 'P':
        if resultado % 2 == 0:
            print('Você Venceu! Continue jogando.')
            vitorias += 1
        else:
            print('Você perdeu! Ganhou o total de {} vitorias'.format(vitorias))
            break
    else:
        print('Digite um valor valido!')


maisde18 = 0
homens = 0
mulhersmenos20 = 0
while True:
    sexo = input('Digite seu sexo: ').upper()
    idade = int(input('Digite sua idade: '))
    print('CADASTRADO COM SUCESSO!')
    if idade > 18:
        maisde18+=1
    if sexo.upper() == 'M':
        homens+=1
    if sexo.upper() == 'F' and idade < 20:
        mulhersmenos20+=1
    status = input('Deseja continuar? [S/N] '.upper())
    if status.upper() == 'N':
        break
    elif status.upper() == 'S':
        print('Continuando...')
    else:
        print('Digite ou N ou S')
        status = input('Deseja continuar? [S/N] ')
print(f'Pessoas com mais de 18: {maisde18}\nHomens Cadastrados: {homens}\nMulheres com menos de 20 anos: {mulhersmenos20}')



mais_barato = 0
menor = 0
cont = 0
barato = ''
maisde1000 = 0
totalcompra = 0
while True:
    nome = input('Nome do Produto: ')
    preco = float(input('Valor do produto: '))
    cont+=1
    print('CADASTRADO!!')
    totalcompra+=preco
    if preco > 1000:
        maisde1000+=1
    if cont == 1:
        menor = preco
        barato = nome
    else:
       if preco < menor:
        menor = preco
        barato = nome
    if preco < menor:
        menor = preco
    status = ' '
    while status not in 'SN':
        status = input('Deseja continuar? {S/N}? ').strip().upper()[0]
    if status == 'S':
        print('Continuando...')
    elif status == 'N':
        break
print(f'O total gasto na compra foi de {totalcompra:.2f} reais\n{maisde1000} produtos custam mais de 1000\nO produto mais barato foi {barato} que custa {menor} reais')






nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota1 = 0
dinheiro = int(input('Retirar R$'))

while dinheiro % 50 == 0:
    nota50+=1
    dinheiro -= 50
print(nota50)





