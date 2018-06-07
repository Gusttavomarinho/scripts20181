#Exercício 05. ​ Crie uma função que recebe como parâmetro uma string e
#imprima cada letra da palavra seguido de um ​ underline ​ . Ex.: input = "Python"
#output = "P_y_t_h_o_n".

#Imprimindo a palavra separado usando estrutura de repetição 
def imprime_separado(palavra):
    for x in range(0,len(palavra)):
        if x == len(palavra) - 1:
            print(palavra[x])
        else:
            print (palavra[x], end='_')

#Imprimindo a palavra separado usando a função join 
def imprime_separado_join(palavra):
    palavra_separada = "_".join(palavra)
    print(palavra_separada)

