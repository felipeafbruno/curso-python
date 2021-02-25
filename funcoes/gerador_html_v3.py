def tag_bloco(conteudo, classe='success', inline=False):  # parametro nomeado
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):  # unpacking
    # gerando uma tupla por meio de um generato com cada item da tupla de itens passado como parametro
    # por fim o join() que vai concatenar cada item da tupla
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    # inline=True -> parametro nomeado já que não é passado o segundo parametro classe
    # esse recurso contonar um possível erro
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=False, conteudo='inline'))
    print(tag_bloco('Falhou', classe="error"))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe="info"))
