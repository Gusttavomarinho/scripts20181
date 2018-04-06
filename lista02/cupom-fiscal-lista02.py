#GUSTAVO HENRIQUE MARINHO DE OLIVERIA - 2018B010153
#declarando as variaveis e recebendo os dados
nome_prudutoA = input("Digite o nome do produto #01:")
valor_ProdutoA = input("Digite o valor do produto #01:")
nome_prudutoB = input("Digite o nome do produto #02:")
valor_ProdutoB = input("Digite o valor do produto #02:")
nome_prudutoC = input("Digite o nome do produto #03:")
valor_ProdutoC = input("Digite o valor do produto #03:")
#preparando para imprimir
total_produtos = (float(valor_ProdutoA) + float(valor_ProdutoB) + float(valor_ProdutoC))
#imprimindo os resultados
print("|{:-<24}|".format("-"))
print("|{:^24}|".format("C U P O M F I S C A L"))
print("| {:<23}|".format("PRODUTO #01"))
print("|  {:<14.13}R${:<5.5} |".format(nome_prudutoA,valor_ProdutoA))
print("| {:<23}|".format("PRODUTO #02"))
print("|  {:<14.13}R${:<5.5} |".format(nome_prudutoB,valor_ProdutoB))
print("| {:<23}|".format("PRODUTO #03"))
print("|  {:<14.13}R${:<5.5} |".format(nome_prudutoC,valor_ProdutoC))
print("| {:<14.13}R${:<6.6} |".format("TOTAL: ",total_produtos))
print("|{:-<24}|".format("-"))


