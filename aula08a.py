import math
import random
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é {:.2f}'.format(num, math.ceil(raiz)))

num1=float(input('Digite um numero: '))
print('O numero é: {:.0f}'.format(num1))






aluno1 = str(input('Informe o nome do 1º aluno: '))
aluno2 = str(input('Informe o nome do 2º aluno: '))
aluno3 = str(input('Informe o nome do 3º aluno: '))
aluno4 = str(input('Informe o nome do 4º aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
print (f'O aluno sorteado é: {random.choice(lista)}')

aluno1 = str(input('Informe o nome do 1º aluno: '))
aluno2 = str(input('Informe o nome do 2º aluno: '))
aluno3 = str(input('Informe o nome do 3º aluno: '))
aluno4 = str(input('Informe o nome do 4º aluno: '))
random.shuffle(lista)
print(f'A ordem dos alunos será: {lista}')