#Exercício 01. ​ Crie um programa que verifique se um valor inteiro inserido pelo
#usuário é maior ou menor que zero.

#Pegando o valor do usuario
valor = int(input("Digite um valor inteiro:"))

#Verificando o valor digitado
if valor > 0 :
    print("O valor digitado é:",valor," Ele e maior que zero")
else:
    print("O valor digitado é:",valor," Ele e menor que zero")
