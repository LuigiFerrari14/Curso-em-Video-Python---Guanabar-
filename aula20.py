def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-' * 30)

mensagem('SISTEMA DE ALUNOS')


#nao sei quantos valores são..... usar o *
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 4)
contador(1, 5, 8, 9, 10)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos+=1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)






#Desafios
def area(largura, comprimento):
    total = largura * comprimento
    print(f'A area do terreno {largura}x{comprimento} é de {total}m2!')

area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))



def responsivo(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)

valor1 = str(input('Digite um texto: '))
responsivo(valor1)

valor2 = str(input('Digite um texto: '))
responsivo(valor2)



import time
def contador(i, f ,p):
    if p < 0:
        p*=-1
    if p == 0:
        p = 1
    if f > i:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for n in range(i, f+1):
            print(n, end=' ')
            time.sleep(0.5)
            n+=p
        print('\n', '-'*30)
    else:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        cont = i
        while cont >=f:
            print(cont, end=' ')
            time.sleep(0.5)
            cont-=p
        print('\n', '-'*30)


contador(1, 10 , 1)

contador(10, 0 , 2)

print('Agora é a sua vez de personalizar a contagem: ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)




def maior(*num):
    cont = 1
    m = 0
    for valor in num:

        if cont == 1:
            m=valor
            cont+=1
        else:
            if valor > m:
                m=valor
    print(f'Foram informados {len(num)} valores ao todo, sendo eles {num}')
    print(f'O maior número é {m}')


maior(2, 9, 4, 5, 7, 1)
print('-'*20)
maior(4, 7, 0)
print('-'*20)
maior(1, 2)
print('-'*20)
maior(6)
print('-'*20)
maior()

import random
numeros = list()
def sorteia(lista):
    print('Sorteando...')
    for n in range(0,5):
        lista.append(random.randint(1,11))

def somapar(lista):
    tot = 0
    for n in lista:
        if n % 2 == 0:
            tot+=n
    print(f'Somando os valores pares, temos: {tot}')

numeros = list()
sorteia(numeros)

print(numeros)
somapar(numeros)










