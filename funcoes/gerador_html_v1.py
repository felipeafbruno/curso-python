def tag_bloco(texto, classe='success'): # parametro padrão 
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    assert tag_bloco('Incluido com sucesso!') == \
        '<div class="success">Incluido com sucesso!</div>'
    assert tag_bloco('Impossível excluir!', 'error') == \
        '<div class="error">Impossível excluir!</div>'
    