#Criando a lista de numeros
lista = [1,2,3,4,5,6,7,8,9]

#Seprando os numeros pares a partir do inicio da lista
numeros_pares = lista[1::2]
#imprimando numeros pares
print(numeros_pares)

#Separando os numeros imprares
numeros_impares = lista[2::2]
#Imprimento numeros impares
print(numeros_impares)


#Seprando os numeros pares de forma invertida
numeros_pares_invertido = lista[1::2]
#invertendo
numeros_pares_invertido.reverse()
#imprimando numeros pares
print(numeros_pares_invertido)

#Separando os numeros impares invertido
numeros_impares_invertido = lista[2::2]
#invertendo
numeros_impares_invertido.reverse()
#Imprimento numeros impares
print(numeros_impares_invertido)
