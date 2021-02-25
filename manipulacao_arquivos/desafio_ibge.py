import csv
import urllib.request
import os.path

url = 'http://files.cod3r.com.br/curso-python/desafio-ibge.csv'

# os.path -> módulo fornece funções que permitem realizar verificações
# sobre arquivos e uma das funções é o exists() para verificar a
# se ele existe ou não
if not os.path.exists('desafio_ibge.csv'):
    # baixando arquivo utilizando o módulo urllib.request
    urllib.request.urlretrieve(url, 'desafio_ibge.csv')


# with - instrução associada a um objeto
# ao entra no bloco executado o método __enter__() do objeto associado
# e o encerrar o método __exit__() do objeto associado
# simulando um try finally
# open() -> dentre os vários propriedades possiveis de se passar na função
# podemos dar o encoding que configurar códificação do arquivo
with open('desafio_ibge.csv', encoding="ISO 8859-1") as arquivo:
    # função DictReader() mapeia cada linha o arquivo csv
    # para um par chave/valor(dicionario)
    for registro in csv.DictReader(arquivo):
        print('Código do Destino: {} e Nome do Destino: {}'.format(
            registro['cod_destin'], registro['nome_desti']))
