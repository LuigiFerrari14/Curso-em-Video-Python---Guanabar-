dados = dict()
dados = {'nome':'Pedro','idade':'25'}
print(dados['idade'])
#adicionar
dados['sexo'] = 'M'
print(dados)
#deletar
del dados['idade']
print(dados)


#------------------------------------------------------
#pega valores V
print(dados.values())

#pegar os titulos ex: nome, idade... K
print(dados.keys())

#pegar todos valores I
print(dados.items())
#------------------------------------------------------


for k, v in dados.items():
    print(f'O {k} é {v}')

#dicionario dentro da lista
brasil = list()
estado1 = {'uf':'Rio de Janiero','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)


#------------------------------------------------------IMPORTANTE
estado = dict()
brasil=list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

#------------------------------------------------------IMPORTANTE




#Desafios
aluno = dict()

aluno['nome'] = str(input('Qual o Nome do Aluno: '))
aluno['media'] = float(input(f'Qual a Media de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}: ')


import random
import time
import operator
cont = 1
jogadores = {'jogador1': random.randint(1,6),
            'jogador2': random.randint(1,6),
            'jogador3': random.randint(1,6),
            'jogador4': random.randint(1,6)}

ranking = list()
for k, v in jogadores.items():
    print(f'{k} tirou o Número {v}')
    time.sleep(1)
print('Ranking dos jogadores: ')
ranking = sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar {v[0]} com {v[1]} pontos!')
    time.sleep(1)

todosjogadores = list()
gols = list()
jogador = dict()
cont = 1
total = 0
jogador['Nome'] = str(input('Qual o nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for p in range(0, partidas):
    gol = (int(input(f'Quantos gols na partida {cont}? ')))
    cont+=1
    total+=gol
    gols.append(gol)
jogador['gols'] = gols
jogador['total'] = total
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for e, p in enumerate(gols):
    print(f'Na partida {e+1}, fez {p} gols. ')
print(f'Foi um total de {total} gols.')




time = list()
gols = list()
jogador = dict()
cont = 1
total = 0
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Qual o nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for p in range(0, partidas):
        gol = (int(input(f'Quantos gols na partida {cont}? ')))
        cont+=1
        total+=gol
        gols.append(gol)
    jogador['gols'] = gols
    jogador['total'] = total
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N]: '.upper()[0]))
        if resposta in 'SN':
            break
        else:
            print('Responda apenas com [S/N]: '.upper()[0])
    if resposta == 'N':
        break

print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for e, p in enumerate(gols):
    print(f'Na partida {e+1}, fez {p} gols. ')
print(f'Foi um total de {total} gols.')


jogadores = list()
jogador = dict()
gols = list()


#       Area de captação dos dados


while True:
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(1, partidas + 1):
        gols.append(int(input(f'    Quantos gols na {p}ª partida? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())


    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        print('ERROR! Por favor, digite S ou N.')
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break


#       Mostrando Resultados
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()


print('-' * 50)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)


opcao = input('Qual jogador voce quer? Digite o codigo: ')
if opcao > len(jogadores):
    print('Não existe!')


