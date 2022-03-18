a = 1
par = 0
impar = 0
while a != 0:
    a = int(input('Digite um valor: '))
    if a != 0 :
        if a % 2 == 0:
         par += 1
        else:
         impar += 1
print('{} numeros pares\n{} numeros impares'.format(par,impar))

#strip remove os espaços, upper deixa em MAIUSCULO e o [0] pega a primeira letra
s = str(input('Digite seu sexo, sendo [M] Masculino ou [F] feminino: ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Dados invalidos! [M] Masculino ou [F] feminino: ')).strip().upper()[0]
print('Bem Vindo {}'.format(s))



import random
aleatorio = random.randrange(1,5)
erro = 0
numero = int(input('Digite um número entre 1 e 5: '))
while aleatorio != numero:
    numero = int(input('Você errou! Digite outro número: '))
    erro+=1
if aleatorio == numero:
    print('Você venceu, gastou {} chances'.format(erro))
else:
    print('Você Perdeu!')



import time
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))


menu = int(input('O que você deseja fazer?\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Números\n[5]Sair do Programa\n-> '))
while menu != 5:
    if menu == 1:
        soma = num1 + num2
        print('A soma de {} + {} = {}'.format(num1,num2,soma))
        time.sleep(2)
        menu = int(input('Concluido! O que você deseja fazer em seguida?\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Números\n[5]Sair do Programa\n-> '))
    elif menu == 2:
        mult = num1 * num2
        print('A multiplicação de {} * {} = {}'.format(num1, num2, mult))
        time.sleep(2)
        menu = int(input('Concluido! O que você deseja fazer em seguida?\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Números\n[5]Sair do Programa\n-> '))
    elif menu == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1,num2))
            time.sleep(2)
            menu = int(input('Concluido! O que você deseja fazer em seguida?\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Números\n[5]Sair do Programa\n-> '))
        elif num2 > num1:
            print('{} é maior que {}'.format(num2,num1))
            time.sleep(2)
            menu = int(input('Concluido! O que você deseja fazer em seguida?\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Números\n[5]Sair do Programa\n-> '))
        else:
            print('Os números são iguais!')
            time.sleep(2)
            menu = int(input('Concluido! O que você deseja fazer em seguida?\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Números\n[5]Sair do Programa\n-> '))
    elif menu == 4:
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite um valor: '))
        menu = int(input('Concluido! O que você deseja fazer em seguida?\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Números\n[5]Sair do Programa\n-> '))




valor = int(input('Digite um valor para fatorar: '))
mult = valor
f = 1
while mult > 0:
    print('{}'.format(mult), end='')
    print(' x ' if mult >1 else ' = ', end='')
    f *= mult
    mult -= 1
print('{}'.format(f))




total = 1
digitados = 1
numero = int(input('Digite um numero: '))
while numero != 999:
    numero = int(input('Digite um numero: '))
    if numero !=999:
        digitados += 1
        total += numero
print('{} foram digitados e a soma entre eles são {}'.format(digitados,total))





pergunta = 'S'
contador = int(1)
total = int(0)
while pergunta.upper() == 'S':
    numero = int(input('Digite um valor: '))
    if contador == 1:
        menor = numero
        maior = numero
    elif numero < menor:
        menor = numero
    elif numero > maior:
        maior = numero
    contador += 1
    total += numero
    pergunta = str(input('Deseja continuar? [S] ou [N]: '.upper()))

contador += -1
media = total/contador
print('{} numero digitados\nMaior = {} e Menor = {}\nMedia = {}'.format(contador,maior,menor,media))
