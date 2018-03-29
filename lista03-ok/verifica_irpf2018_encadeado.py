#Verificando se precisa declarar imposto de renda


#recebendo dados do usuario

print("Realizou operações financeiras na bolsa de valores \n, ou de compra e venda de capital estrangeiro ?")
pergunta_a = int(input("Digite 1 = sim , 0 = Não :"))

print("Tem bens (casas, carros, terras, etc) \n cujo valor de venda totalizem acima de R$300.000,00?")
pergunta_b = int(input("Digite 1 = sim , 0 = Não :"))

print("Teve rendimentos não tributáveis, \n no ano anterior, cujo valor superasse R$ 40.000,00?")
pergunta_c = int(input("Digite 1 = sim , 0 = Não :"))

print("Teve rendimentos tributáveis durante o ano de 2017, \n cujo valor superasse a faixa de R$ 28.123,00?")
pergunta_d = int(input("Digite 1 = sim , 0 = Não :"))


#Fazendo as verificações

if pergunta_a == 1 or pergunta_b == 1 or pergunta_c == 1 or pergunta_d == 1 :
    print("Voce precisa fazer a declaração do imposto de renda")
elif pergunta_a == 0 and pergunta_b == 0 and pergunta_c == 0 and pergunta_d == 0 :
    print("Voce não precisa fazer a declaração do imposto de renda 'Gloria a Deus' ")


