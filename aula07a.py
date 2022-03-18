nome = input('Qual seu nome? ')
print('Bem Vindo {:*^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
d = n1 / n2
print('A soma é {} \n e a divisão é {:.2f} '.format(s,d))

numero = int(input('Digite um número: '))
s = numero + 1
a = numero - 1
dobro = numero * 2
triplo = numero * 3
raiz = (numero ** (1/2))
print('O seu sucessor é {} e seu antecessor é {}'.format(s,a))
print('Dobro = {}\nTriplo = {}\nRaiz = {}'.format(dobro,triplo,raiz))

nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))
notatotal = nota1 + nota2
media = notatotal / 2
print('A media do aluno é {:.2f}'.format(media))

dinheiro = float(input('Quantos reais você tem: '))
dolar = float(3.27)
comprar = dinheiro/dolar
print('Você pode comprar {:.2f} Dolar(es)'.format(comprar))

altura = int(input('Altura da parede: '))
largura = int(input('Largura da parede: '))
area = altura * largura
balde = int(2)
qtsbaldes = area/balde
print('Você vai precisar de {} baldes de tinta'.format(qtsbaldes))

precoproduto = int(input('Qual o preco do produto: '))
desconto = precoproduto*0.05
precocomdesconto = precoproduto-desconto
print('O preço do produto com desconto de 5% será de: {:.2f} reais'.format(precocomdesconto))

salarioatual = int(input('Salario Atual: '))
aumento = salarioatual*0.15
salariocomaumento = salarioatual + aumento
print('O salario com 15% de aumento será de {} reais'.format(salariocomaumento))