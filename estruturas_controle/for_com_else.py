PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('O texto contem pelo menos uma palavra uma palavra proibida: ', palavra)
            found = True
            break
    else:
        print('O texto não contem palavra proibida: ', texto)
