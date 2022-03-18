def contador(i,f,p):
    """
    -> Faz uma contagem
    i=inicio
    f=fim
    p=passo
    """
    c = i
    while c <= f:
        print(f'{c}',end='..')
        c+=p
    print('FIM!')

help(contador)
contador(2,10,2)

#Valor não informado colocar =x. Caso seja informado irá pegar o valor informado, caso n, pegara o valor q vc colocou apos o =
def somar(a,b,c=0):
    s=a+b+c
    #print(f'A soma é: {s}')
    return s


resp = somar(4,4)
resp2 = somar(6,4)
print(f'As somas valem: {resp},{resp2}')



def funcao(b):
    #global faz com que o valor digitado na função passe a ser o "ORIGINAL"
    global a
    a=8
    b+=4

    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')

a=5
funcao(a)
print(f'A fora vale: {a}')




def fatorial(num=1):
    f=1
    for c in range(num, 0, -1):
        f*=c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
f=fatorial()
print(f)


import datetime
def voto(ano):
    anoatual = datetime.date.today().year
    idade = anoatual - ano
    if idade > 64 or idade == 16 or idade == 17:
        return f'Com {idade} anos. Seu voto é: Voto Opcional'
    elif idade <= 16:
        return f'Com {idade} anos. Seu voto é: NEGADO'
    else:
        return f'Com {idade} anos. Seu voto é: OBRIGATORIO'

ano = int(input('Digite seu ano de Nascimento: '))
print(voto(ano))




def fatorial(num, show=False):
    f=1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f*=c
    return f




print(fatorial(5, show=True))



def ficha(jog='Desconhecido',gol='0'):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)


def leiaint(num):
    valor = 0

    while True:
        n=str(input(num))
        if n.isnumeric():
            valor = n
            break
        else:
            print('Erro! Digite um Número Valido!')

    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')




def notas(num, sit=False):

    dictnt = dict()
    dictnt['total'] = len(num)
    dictnt['maior'] = max(num)
    dictnt['menor'] = min(num)
    dictnt['média'] = sum(num)/len(num)
    print(type(num))
    if sit:
        if dictnt['média'] >= 9:
            dictnt['sit'] = 'ÓTIMA'
        elif dictnt['média'] >= 7:
            dictnt['sit'] = 'BOA'
        elif dictnt['média'] >= 5:
            dictnt['sit'] = 'REGULAR'
        else:
            dictnt['sit'] = 'RUIM'
    return dictnt


#Programa Principal
nota = list()
cont = 1
print('Digite as notas dos alunos!')
while True:
    resp = float(input(f'Digite a nota do {cont}º aluno: '))
    nota.append(resp)
    d = input('Deseja continuar [S/N]? ')
    cont+=1
    if d in 'nN':
        break
print(notas(nota, sit=True))