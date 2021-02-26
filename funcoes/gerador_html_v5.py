bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')

# gerando um dicionario apartir do 'informados' que é uma 'kwargs' passada para a função 
# e filtrando aqueles que são necessários para cada situação   
def filtro_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"' for k, v in informados.items() if k in suportados)


# parametro nomeado, *args esta fazendo o packing de dos valore Sabado e Domingo
# como existe um parametro packing é necessário passar para a função
# todos os outros parametros como nomeados para não ocorrer qualquer tipo de erro
def tag_bloco(conteudo, *args, classe='success', inline=False, **novo_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **novo_atrs)
    atributos = filtro_atrs(novo_atrs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novo_atrs):  # unpacking
    # gerando uma tupla por meio de um generato com cada item da tupla de itens passado como parametro
    # por fim o join() que vai concatenar cada item da tupla
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    atributos = filtro_atrs(novo_atrs, ul_atrs)
    return f'<ul {atributos}>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    # inline=True -> parametro nomeado já que não é passado o segundo parametro classe
    # esse recurso contonar um possível erro
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=False, conteudo='inline'))
    print(tag_bloco('Falhou', classe="error"))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe="info"))
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info', inline=True))
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista', ul_blabla="abc", ul_style="color:red"))
