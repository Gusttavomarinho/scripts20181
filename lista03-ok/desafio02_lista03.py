#Tentando acerta o numero sorteado

#importando as bibliotecas
from random import randint

sorteio = randint(0,50)
tentativa = 1
#gerando as tentativas

while( tentativa < 4):
    if tentativa == 1 :
        numero_palpite =  int(input("Tentativa #1: Adivinhe um valor entre 0 e 50:"))
        if sorteio < numero_palpite:
            print("O numero sorteado e menor")
        if numero_palpite == sorteio:
            print("Voce acertou numero sorteado foi:",sorteio)
            tentativa = 100
        else:
            print("tente novamente")
    tentativa = tentativa + 1
    if tentativa == 2 :
        numero_palpite =  int(input("Tentativa #2: Adivinhe um valor entre 0 e 50:"))
        if sorteio > numero_palpite:
            print("O numero sorteado e maior")
        if numero_palpite == sorteio:
            print("Voce acertou numero sorteado foi:",sorteio)
            tentativa = 100
        else:
            print("tente novamente")
    tentativa = tentativa + 1

    if tentativa == 3 :
        numero_palpite =  int(input("Tentativa #3: Adivinhe um valor entre 0 e 50:"))
        if sorteio < numero_palpite and not sorteio % 2 == 0:
            print("O numero sorteado e menor e impa")
        if numero_palpite == sorteio:
            print("Voce acertou numero sorteado foi:",sorteio)
            tentativa = 100
        else:
            print("tente novamente")
    tentativa = tentativa + 1

    if tentativa == 4 :
        numero_palpite =  int(input("Tentativa #4: Adivinhe um valor entre 0 e 50:"))
        if numero_palpite == sorteio:
            print("Voce acertou numero sorteado foi:",sorteio)
            tentativa = 100
        else:
            print("Voce errou todas as tentativas , Xau")
