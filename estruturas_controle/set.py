PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

for texto in textos:
    interseccao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().spli()))
    if interseccao:
        print('Texto possui palavras proibidas: ',interseccao)
    else:
        print('Texto autorizado: ', texto)