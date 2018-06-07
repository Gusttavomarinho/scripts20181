'''Exercício 09. ​ Crie um menu onde o usuário pode escolher quais das funções
do exercício 08 será chamada. O programa deve imprimir o resultado e solicitar
que o usuário escolha uma outra função. O menu deve possuir uma opção de
saída do programa. Ex.
menu = """
======= MENU =======
1) SOMA(A, B)
2) SUBTRACAO(A, B)
3) MULTIPLICACAO(A, B)
4) DIVISAO(A, B)
5) SAIR DO PROGRAMA
'''
#Definindo as funções 
def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    return a / b

#Criando a repetição e o menu do programa 
opcao = 0
while(opcao != 5):
    print("=======MENU=======")
    print("1) SOMA")
    print("2) SUBTRAÇÃO")
    print("3) MULTIPLICAÇÃO")
    print("4) DIVISÃO")
    print("5) SAIR DO PROGRAMA")
    opcao = int(input("Digite uma opção do menu: "))
    #Recebe os numeros digitados pelo usuario para passar para função que o if vai chaamar
    if opcao == 5:
        break 
    if opcao > 0 and opcao < 5:
        numero_a = float(input("Digite um numero: "))
        numero_b = float(input("Digite outro numero: "))
        if opcao == 1:
            resultado =soma(numero_a,numero_b)
            print("O resultado da operação escolhida e",resultado)
        elif opcao == 2:    
            resultado = subtracao(numero_a,numero_b)
            print("O resultado da operação escolhida e",resultado)
        elif opcao == 3:    
            resultado = multiplicacao(numero_a,numero_b)
            print("O resultado da operação escolhida e",resultado)
        elif opcao == 4:    
            resultado = multiplicacao(numero_a,numero_b)
            print("O resultado da operação escolhida e",resultado)
    else:
        print("Opção digitada e invalida")