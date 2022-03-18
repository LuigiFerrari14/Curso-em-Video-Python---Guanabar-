tempo = int(input('Quantos anos tem seu carro? '))
if tempo > 5:
    print('Seu carro está velho!')
else:
    print('Seu carro está novo!')


n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
print('Sua média foi: {:.1f}'.format(m))
if m >= 6:
    print('\033[32mSua média foi Boa!!\033[m')
elif m >= 3:
    print('\033[33mSua média foi mediana!\033[m')
else:
    print('\033[31mSua média foi ruim!\033[m ')

import random
aleatorio = random.randrange(1,5)
numero = int(input('Digite um número entre 1 e 5: '))
if aleatorio == numero:
    print('Você venceu!')
else:
    print('Você Perdeu!')

velocidade = int(input('Qual a velocidade do Carro? '))
velocidademaxima = int(80)
multa = int(7)
if velocidade > velocidademaxima:
    amais = velocidade - velocidademaxima
    pagar = amais * multa
    print('Você passou {}kg e sua multa será de {:.2f} reais'.format(amais,pagar))
else:
    print('Você passou dentro do limite!')

numero = int(input('Digite um numero: '))
resultado = numero%2
if resultado == 1:
    print('O número é impar!')
else:
    print('O número é par')


