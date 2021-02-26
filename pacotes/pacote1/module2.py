def main():
    print('Rodando o main() no módulo {__name__}')

# esse trecho de código nã0 é uma boa prática
# nunca tente executar o módulo no momento do carregamento 
# por que isso não vai executar corretamente 
if __name__ == '__main__':
    main()