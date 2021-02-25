# Versão da aula
def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Final de Semana',
        tuple(range(1, 7)): 'Dia da Semana'
    }
    # generator que retorna o tipo com base no iteração sobre
    # chave/valor e na condicional do dia passado por parametro na chave dias da iteração
    dia_escolhido = (tipo for dias, tipo in dias.items() if dia in dias)
    return next(dia_escolhido, '** Dia Inválido **')


if __name__ == '__main__':
    for dia in range(1, 8):
        print(f'{dia}: {get_tipo_dia(dia)}')


# Minha Versão antes de assistir o vídeo
def get_tipo_dia(dia_escolhido):
    dias = {
        (1, 7): 'Final de Semana',
        tuple(range(1, 7)): 'Dia da Semana'
    }
    for dia, tipo in dias.items():
        if dia_escolhido in dia:
            return tipo


if __name__ == '__main__':
    tupla = (i for i in range(1, 8))
    for dia in tupla:
        print(f'dia {dia} e {get_tipo_dia(dia)}')
