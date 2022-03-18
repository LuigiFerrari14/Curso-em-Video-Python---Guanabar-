frase = '   Curso em Vídeo Python  '
#len conta quantos caracteres tem na frase --
print(len(frase[:21]))
#frase.count - 'x' valor q vc quer saber quantos tem --- 0,13 significa do caracter 0 até o 12!
print(frase.count('o',0,13))
#mostra em que momento começou o valor digitado entre ''
print(frase.find('deo'))
#Existe a palavra digitada entre '' TRUE OR FALSE
print('Curso' in frase)
#substitui
print(frase.replace('Python','Apple'))
#maicuslo
print(frase.upper())
#minusculo
print(frase.lower())
#so o primeiro caractere fica maisuclo
print(frase.capitalize())
#Primeira letra de cada palavra maiusculo
print(frase.title())
#remove todos espaços do inicio e do final
print(frase.strip())
#remove todos espaços da direita
print(frase.rstrip())
#remove todos espaços da esquerda
print(frase.lstrip())
#cada palavra fica separada
print(frase.split())
#insere o valor digitado depois de cada palavra
print('-'.join(frase))

#unir dois comando
print('-'.join(frase.split()))


#digitar um texto maior, usar 3 aspas """
print("""oisaoi doiasoikdo asidois aodio asidoasid a
i oadioasi odiasoi doisaodasok lasd sad
 dasd
apks d asjdo osajdkoasopjkoi xsjkfds""")


#salvar alteração de mudanca da frase
frase = frase.replace('Python','Apple')
print(frase)

#exibir somente a palavra desejada // primeiro [] = numero da palavra // segundo [] = numero da letra
dividido = frase.split()
print(dividido[2][3])