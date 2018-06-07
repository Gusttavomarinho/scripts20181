#Exercício 04. ​ Crie uma função que recebe como parâmetro um número real ​ n
#e retorna True caso o número seja par.

#Criando a função e verificando se o numero e par 
def numero_real_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

#obs: para usar esta função no interpretador python , from q04 import numero_real_par
