#Exercício 03. ​ Crie uma função que recebe como parâmetro um número real ​ n
#e retorna True caso seja 0 (zero) ou positivo e False caso seja menor que zero.

#Criando a função e verificando se o numero e maior que zero
def numero_real(numero):
    if numero > 0:
        return True
    else:
        return False

#obs: para usar esta função no interpretador python , from q03 import numero_real