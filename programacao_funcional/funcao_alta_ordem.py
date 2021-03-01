from funcao_primeira_classe import dobro, quadrado

# High Order Function(Função de Alta Ordem)
'''
    Python permite a passagem de função com parametro para outra função
    e também um função retorna outra função
'''
def processar(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))


if __name__ == '__main__':
    processar('Dobros de 1 a 10', range(1, 10), dobro)
    processar('Quadrados de 1 a 10', range(1, 10), quadrado)