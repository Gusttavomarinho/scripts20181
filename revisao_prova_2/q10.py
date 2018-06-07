'''Exercício 10. ​ Crie um programa que peça que o usuário insira valores reais
até que ele insira 0. Os valores inseridos pelo usuário devem ser acumulados
(soma). Após o usuário digitar 0 (zero) o programa deverá imprimir o valor
acumulado.
'''
#Iniciando o contador
numero = 1
soma = 0
while numero != 0:
    numero = int(input("Digite um numero:"))
    print("Para sair do programa Digite 0 , ele retorna sua soma")

    soma = numero + soma
    
else:
    print("A soma dos valores digitados é:",soma)




