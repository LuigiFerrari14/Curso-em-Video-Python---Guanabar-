valorcasa = float(input('Qual é o valor da Casa? '))
salarios = float(input('Qual seu salario? '))
tempo = int(input('Quantos anos vai pagar: '))
total = valorcasa / tempo
if total > salarios * 0.3:
    print('Infelizmente você não pode comprar esta casa!')
else:
    print('Você poderá pagar a casa, basta pagar {:.2f} reais por mês!'.format(total))





numero = int(input('Digite um número: '))
converter = int(input('Digite 1 para Binario, 2 para Octal e 3 Para Hexadecimal: '))
if converter == 1:
    print(bin(numero))
elif converter == 2:
    print(oct(numero))
else:
    print(hex(numero))




num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))

if num1 > num2:
    print('{} é maior que {}'.format(num1,num2))
elif num2 > num1:
    print('{} é maior que {}'.format(num2,num1))
else:
    print('Os dois valores são iguais!')




from datetime import date
anonascimento = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
calculo = anoatual - anonascimento

if calculo == 18:
    print('Está na hora de se alistar')
elif calculo > 18:
    print('Já passou {}ano(s) dá hora de se alistar'.format(calculo - 18))
else:
    print('Você terá que se alistar em {}ano(s)'.format(18 - calculo))



import datetime
anonascimento = int(input('Digite o ano de seu nasciemnto: '))
anoatual = datetime.date.today().year
calculo = anoatual - anonascimento

if calculo < 10:
    print('Mirim')
elif calculo < 15:
    print('Infantil')
elif calculo <= 20:
    print('Senior')
else:
    print('Master')


import random
escolha = int(input('Escolha 0-Pedra, 1-Papel ou 2-Tesoura: '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0,2)
print('o Computador escolheu {}'.format(itens[computador]))
print('o jogador escolheu {}'.format(itens[escolha]))

if computador == 0:
    if escolha == 0:
        print('Empate!')
    elif escolha == 1:
        print('O computador escolheu {} e perdeu!'.format(itens[computador]))
    elif escolha == 2 :
        print('Você perdeu, pois o computador escolheu {}!'.format(itens[computador]))
    else:
        print('Jogada Invalida!')
elif computador == 1:
    if escolha == 0:
        print('Perdeu!')
    elif escolha == 1:
        print('Empate')
    elif escolha == 2 :
        print('Você venceu, pois o computador escolheu {}!'.format(itens[computador]))
    else:
        print('Jogada Invalida!')
elif computador == 2:
    if escolha == 0:
        print('Venceu!')
    elif escolha == 1:
        print('O computador escolheu {} e venceu!'.format(itens[computador]))
    elif escolha == 2 :
        print('empate, pois o computador escolheu {}!'.format(itens[computador]))
    else:
        print('Jogada Invalida!')














