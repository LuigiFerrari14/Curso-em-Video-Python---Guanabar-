for c in range(0,5):
    print('Passo')



for a in range(3, 0, -1):
     print('Em ordem decrecente basta adicionar o -1 no final -- {}'.format(a))


for t in range(0, 6, 2):
     print('O ultimo valor define como sera a contagem, no caso irá pular de 2 em 2 -- {}'.format(t))


s = 0
for w in range(0,4):
    n = int(input('Digite um valor: '))
    #s = s + n é a mesma coisa que s += n
    s+=n
print('A soma entre os números é de: {}'.format(s))


import time
for f in range(10, 0-1, -1):
    time.sleep(1)
    print(f)
print('Feliz Ano novo!!')



s = 0
for n in range(1, 500, 2):
    if(n % 3 == 0):
        s+=n
print(s)



n = int(input('Digite o valor que você quer ver a tabuada: '))
q=0

for x in range(0, 10):
    q= n * x
    print('{} * {} = {}'.format(n, x, q))


s = 0
for x in range(0, 3):
    n = int(input('Digite um valor: '))
    if n%2 == 0:
        s += n
print('A soma dos numeros pares é: {}'.format(s))



n = int(input('Digite um numero: '))
t=0
for x in range(1, n + 1):
    if n%x==0 :
        t = t+1
if t == 2:
    print('O número é Primo')
else:
    print('O número não é primo')




palavra = input('Digite uma frase: ')

print(''.join(palavra.split()))
if palavra == (palavra[::-1]):
    print('é')
else:
    print('não')



import datetime
ano = datetime.date.today().year
maioridade = 18
contador = 0
for x in range(0,7):
    nascimento = int(input('Em que ano você nasceu: '))
    if ano - nascimento >= maioridade:
        contador += 1
print('{} são maiores de idade!'.format(contador))











