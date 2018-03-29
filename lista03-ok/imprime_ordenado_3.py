#Imprimir numeros float ordem crescente

numero_a = float(input("Digite primeiro numero float exemplo: 10.50 :"))
numero_b = float(input("Digite segundo numero float exemplo: 1.30 :"))
numero_c = float(input("Digite terceiro numero float exemplo: 200.23 :"))
print("Agora vamos imprimir em ordem crescente \O/  \n")

#preparando para imprimir

numeros = [numero_a,numero_b,numero_c]

resultado = sorted(numeros, reverse=False)

print(resultado[0],"\n")
print(resultado[1],"\n")
print(resultado[2],"\n")

#outra saida organizada

print(resultado[0],"<=",resultado[1],"<=",resultado[2])

#fim do programa
# Autor : gusttavomarinho@gmail.com
