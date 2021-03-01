class Humano:
    # atributo de classe
    '''
        Em Python para um atributo será de classe 
        ele deve ser criado diretamente dentro dela
        diferente de outras linguagens onde o atributo 
        criado dentro da classe pode ser de instância ou de classe.
        Em Python atributos criados de qualquer método é um 
        atributo de instância
    '''
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Home Neanderthalensis'
        return self


if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')    