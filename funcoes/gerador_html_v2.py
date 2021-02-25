def tag_bloco(texto, classe='success', inline=False): # parametro nomeado
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    # inline=True -> parametro nomeado já que não é passado o segundo parametro classe
    # esse recurso contonar um possível erro
    print(tag_bloco('inline', inline=True)) 
    print(tag_bloco(inline=False, texto='inline')) 
    print(tag_bloco('Falhou', classe="error"))