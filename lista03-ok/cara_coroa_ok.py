#Programa para  aprender a usar random no python

#importando as bibliotecas
from random import randint


#Recebendo os valores do usuario

palpite = input(("Moeda vai ser cara ou coroa ? :"))

#Sorteando 0 = cara , 1 = coroa

sorteio =  randint(0,1)
#verificando e imprimindo o resultado para o usuario

if palpite == "Cara" and sorteio == 0 :
    print("Voce digitou:",palpite)
    print("\n E acertou parabens")
elif palpite == "Coroa" and sorteio == 1 :
    print("Voce digitou:",palpite)
    print("\n E acertou parabens")
else:
    print("Voce digitou:",palpite)
    if sorteio == 1 :
        print("Errou pois a moeda deu # Coroa #")
    else:
        print("Errou pois a moeda deu  # Cara #")
