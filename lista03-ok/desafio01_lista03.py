#Programa que recebe do usuário posições no tabuleiro do
#jogo da velha we verifica se houve um vencedor.

#Dados do script
__author__="Gustavo Henrique"
__version__=1.1
__email__="aluno@unirn.edu.br"
# String de formatação do tabuleiro
tabuleiro="""
{:^3}|{:^3}|{:^3}
{:^3}|{:^3}|{:^3}
{:^3}|{:^3}|{:^3}
"""
# As 9 posições do tabuleiro recebem uma string vazia
"""
(0,0) | (0, 1) | (0, 2)
(1,0) | (1, 1) | (1, 2)
(2,0) | (2, 1) | (2, 2)
"""
p00 = p01 = p02 = p10 = p11 = p12 = p20 = p21 = p22 = ' '
# Insere o valor ? para indicar ao usuário qual posição
# está sendo inserida
p00 = '?'
# Imprime o tabuleiro para o usuário
print(tabuleiro.format(p00, p01, p02,
 p10, p11, p12,
 p20, p21, p22))
# Pede que o usuário insira o valor daquela posição
p00=input("Digite x/o da posição '?':").lower()
# Repete o processo para cada posição
p01 = '?'
print(tabuleiro.format(p00, p01, p02,
 p10, p11, p12,
 p20, p21, p22))
p01=input("Digite x/o da posição '?':").lower()
p02 = '?'
print(tabuleiro.format(p00, p01, p02,
 p10, p11, p12,
 p20, p21, p22))
p02=input("Digite x/o da posição '?':").lower()
p10 = '?'
print(tabuleiro.format(p00, p01, p02,
 p10, p11, p12,
 p20, p21, p22))
p10=input("Digite x/o da posição '?':").lower()
p11 = '?'
print(tabuleiro.format(p00, p01, p02,
 p10, p11, p12,
 p20, p21, p22))
p11=input("Digite x/o da posição '?':").lower()
p12 = '?'
print(tabuleiro.format(p00, p01, p02,
 p10, p11, p12,
 p20, p21, p22))
p12=input("Digite x/o da posição '?':").lower()
p20 = '?'
print(tabuleiro.format(p00, p01, p02,
 p10, p11, p12,
 p20, p21, p22))
p20=input("Digite x/o da posição '?':").lower()
p21 = '?'
print(tabuleiro.format(p00, p01, p02,
 p10, p11, p12,
 p20, p21, p22))
p21=input("Digite x/o da posição '?':").lower()
p22 = '?'
print(tabuleiro.format(p00, p01, p02,
 p10, p11, p12,
 p20, p21, p22))
p22=input("Digite x/o da posição '?':").lower()



# Imprime estado final para o usuário
print('​\n​' +
 "*" * 20 + '​\n​'+
 '\n' +
 'Resultado:​\n​')
# Verifica se houve um vencedor na primeira linha
"""
x | x | x o | o | o
? | ? | ? OU ? | ? | ?
? | ? | ? ? | ? | ?
"""
if(p00 == p01 == p02):
 print("{} Venceu!".format(p00))
#########################################################
# Insira os outros testes aqui <<<<<<<<<<<<<<<<<<<<<<< #
#########################################################
else:
 print("Deu velha! X(")
print(tabuleiro.format(p00, p01, p02,
 p10, p11, p12,
 p20, p21, p22))
