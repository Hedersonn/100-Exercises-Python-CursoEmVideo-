#Importação
from time import sleep
from random import randint

#Escolha aleatória
computador = randint(1, 3)

#Interação
escolha = int(input('''Digite:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
-> '''))
#Frase JOKENPO
sleep(0.80)
print('JO..')
sleep(0.5)
print('KEN..')
sleep(0.5)
print('PO')
sleep(0.5)

#Mudar numero por letra
if computador == 1:
    print('Pedra')
elif computador == 2:
    print('Papel')
elif computador == 3:
    print('Tesoura')
elif computador != 1 or 2 or 3:
    print('Invãlido')
sleep(0.5)
print('Aguardando Resposta...')
sleep(3)

#Identificar quem ganhou
if escolha == computador:
    print('Empate!')
elif escolha == 1 and computador == 2:
    print('Ganhei! HAHAH!')
elif escolha == 1 and computador == 3:
    print('Perdi!')
elif escolha == 2 and computador == 1:
    print('Perdi!')
elif escolha == 2 and computador == 3:
    print('Ganhei! HAHAH!')
elif escolha == 3 and computador == 1:
    print('Ganhei! HAHAH!')
elif escolha == 3 and computador == 2:
    print('Perdi!')