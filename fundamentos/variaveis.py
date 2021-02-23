lista = [1, 2, 3, 4]
dicionario = {"nome": "Felipe", 'idade': 26}

# Python não é uma "linguagem tipada"  
# O tipo é inferido no momento que o código é interpretado
a = 10
b = 5
print(a + b)

a = "Olá mundo Python"
print(a + b)

#  print(a + b) a linha não vai ser executada causando um erro por causa
#  da tentativa de operar uma "+" de um valor sobre uma string o que o python não vai interpretar 
#  esse tipo de operação causa uma ambiguidade que torna dificil para o interpretador saber se esta 
#  executando uma soma ou concatenação