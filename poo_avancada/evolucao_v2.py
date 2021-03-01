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

    # método estático
    # Em Python método estático não receber nenhum parametro
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo + {especie}' for especie in adjetivos)

    # método de classe
    # Em Python método de classe recebe como parametro a classe
    ''' 
        Em um método de classe temos o conceito de Polimorfismo
        pelo fato de que o método recebe a classe como parâmetro
    '''
    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]

class Neanderthalensis(Humano):
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    grokn = Neanderthalensis('Grokn')
    print(f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da instância): {", ".join(jose.especies())}')
    '''
        Nas duas situções abaixo onde a Classe esta acessando diretamente o método
        isso não seria possível caso o método fosse estático
    '''
    print(f'Homo Sapiens evoluído: {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluído: {Neanderthalensis.is_evoluido()}')
    print(f'José evoluído: {jose.is_evoluido()}')
    print(f'Grokn evoluído: {grokn.is_evoluido()}')