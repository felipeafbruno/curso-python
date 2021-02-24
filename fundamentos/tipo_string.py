nome = 'Felipe Bruno'
# Assim como outras linguagens é possivel acessar as posições igual um array
print(nome[0])

# 'marca d'agua'
print("Dias D'Avila" == 'Dias D\'Avila')
print('Teste \" funciona!')
texto = 'Texto ccom apóstrofes pode ter "aspas"'
print(texto)

doc1 = """Texto com multiplas\n\tlinhas """
print(doc1)
doc2 = '''Também é possível 
    com aspas simples'''
print(doc2)

# Funcionalidades operadas sob Strings
nome = 'Felipe Bruno'
print(nome[0])
print(nome[5])
print(nome[-3])
print(nome[4:]) # acessando um range apartir da posição 4 até o fim -> [4:] 
print(nome[-5:])
print(nome[:3]) # acessando um range apartir do inicio até a posição 2 desconsiderando a 3 -> [:3]
print(nome[2:5]) # acessando um range apartir da posição 2 até a posição 4 desconsiderando a 5 -> [2:5]

numeros = '12345678'
print(numeros[::2]) # retorna a string pulando de 2 em 2
print(numeros[1::2]) # retorna a string apartir do indice 1 pulando de 2 em 2
print(numeros[::-1]) # retorna a string invertida


frase = "Python é uma linguagem muito interessante"
print('py' in frase)
print('ing' in frase)
print('py' not in frase)
print(len(frase)) # retorna o tamanho da string
print(frase.lower()) # transforma os caracteres em caixa-baixa/lower-case
print(frase.upper()) # transforma os caracteres em caixa-alta/upper-case
print(frase.split()) # quebra a frase nos espaços em branco
frase = frase.upper()
print(frase.split('E')) # quebra a frase nos espaços em branco