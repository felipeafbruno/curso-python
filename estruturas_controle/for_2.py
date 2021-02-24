palavra = 'paralelepípedo'
for letra in palavra: # percorrendo letras de um string com a estrutura for
    print(letra, end=",") # end -> defini uma formatação de para o print
print('Fim')

aprovados = ['Felipe', 'Bernardo', 'Furtuna']
for nome in aprovados:
    print(nome)

# enumerate() gera um indice para cada iterável ou cada elemento da lista no caso
for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)

dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábada')
for dia in dias_semana:
    print(f'Hoje é {dia}')

for letra in set('muito interessante'):
    print(letra)