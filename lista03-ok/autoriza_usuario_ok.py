usuario = "Administrador"
grupo = "Administradores"

""""" A QUESTAO ! C ! DO EXERCICIO 01 DA LISTA 03 SOLICITA QUE DEMONSTRE AS DIFERENÇAS ENTRE OS IF LISTADOS ABAIXO
POIS BEM VOU ESTAR ESCREVENDO AQUI POR MEIO DE COMENTARIO NO CODIGO E DEPOIS GERANDO O TXT SO COM AS RESPOSTAS E POSTANDO NO GITHUB
"""


# ESTE IF ESTA VEFIFICANDO SE O USUARIO E UM ADMINISTRADOR NO CASO SE O LOGIN DELE POR EXEMPLO O NOME E ADMINISTRADOR

#IF A
if usuario == "Administrador":
 print("Usuário autorizado")
else:
 print("Usuário não é um administrador")

# ESTE IF ESTA VERIFICANDO SE O GRUPO DO USUARIO SE CHAMA ADMINISTRADORES , SE FOR ELE AUTORIZA SE NAO ELE NEGA

# IF B
if grupo == "Administradores":
 print("Usuário autorizado")
else:
 print("Usuário não faz parte do grupo Administradores")

 # ESTE IF ESTA VERIFICANDO SE O USUARIO ADMINISTRADOR PERTENCE AO GRUPO ADMINISTRADORES

# IF C
if usuario == "Administrador" and grupo == "Administradores":
 print("Usuário autorizado")
else:
 print("Usuário não autorizado")

# ESTE IF ESTA VERIFICANDO SE O USUARIO ADMINISTRADORES OU O GRUPO ADMINISTRADORES ESTA ACESSANDO O SISTEMA CASO UMA DAS CONDIÇÕES SEJA VERDADEIRA ELE ACEITA O ACESSO


# IF D
if usuario == "Administradores" or grupo == "Administradores":
 print("Usuário autorizado")
else:
 print("Usuário não autorizado")
