#Exercício 07. ​ Crie uma função que recebe como parâmetro uma string e
#imprima a quantidade de consoantes e de vogais da string.

def conta_vogais_consoantes(palavra):
    vogais = 0
    consoantes = 0
    for caracter in palavra:
        if caracter in 'aeiou':
            vogais = vogais + 1
        else:
            consoantes = consoantes + 1

    print("Quantidade de vogais:",vogais)
    print("Quantidade de consoantes:",consoantes)
