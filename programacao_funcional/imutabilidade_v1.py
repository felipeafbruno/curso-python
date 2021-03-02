from locale import setlocale, LC_ALL
from calendar import month_name, mdays
from functools import reduce


# Aplicando Date para Português
setlocale(LC_ALL, 'pt-BR')

# Listar todos os meses do ano com 31 anos
# minha versão
meses = list(map(lambda i: i, range(1, 13)))
meses_31 = list(filter(lambda mes: mdays[mes] == 31, meses))


def frase(mes):
    return f'{month_name[mes].capitalize()} tem {mdays[mes]} dias'


frases = list(map(frase, meses))
print(frases)

# versão da curso
frases = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
                map(lambda mes: month_name[mes],
                    filter(lambda mes: mdays[mes] == 31, range(1, 13))), 'Meses com 31 dias')

print(frases)
