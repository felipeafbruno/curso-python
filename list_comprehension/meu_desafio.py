def procurar_nome(nome_escolhido):
    nomes = {
        1: 'Felipe',
        2: 'Bernardo',
        3: 'Furtuna',
        4: 'Pedro',
        5: 'Bernardete'
    }
    nome_encontrado = (nome for id, nome in nomes.items() if nome_escolhido == nome)
    return next(nome_encontrado, '** Nome não encontrado!!! **')

if __name__ == '__main__':
    print(procurar_nome('Brnardo'))