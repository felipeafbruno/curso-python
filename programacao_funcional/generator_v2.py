from generator_v1 import cores_arco_iris


if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))
    # diferenta da versão 1 utilizando o next()
    # o for aplica um tratamento para exceção StopIteration
    for cores in generator: # Lazy Evaluation
        print(cores)
