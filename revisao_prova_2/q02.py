#Exercício 02. ​ Crie um programa que recebe dois valores reais inseridos pelo
#usuário e imprima o maior deles.

#Recebendo os valores float do usaurio
valor_01 = float(input("Digite um valor real:"))
valor_02 = float(input("Digite outro valor real:"))

#Verificando qual o valor e maior 
if valor_01 > valor_02:
    print("O valor maior é:",valor_01)
else:
    print("O valor maior é",valor_02)
