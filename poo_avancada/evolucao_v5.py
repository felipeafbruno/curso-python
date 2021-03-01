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
        self._idade = None  # atributo "privado"

    # método abstrato
    # método sem implementação
    @property
    def inteligente(self):
        raise NotImplementedError('Propriedades não implementadas')

    '''
        @property - permite que o atributo seja acessado diretamente
        sem que os métodos que altera ou retorno tenham que ser invocados
    '''
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo!')
        self._idade = idade

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

    # definição do método abstrato da classe Humano
    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    # definição do método abstrato da classe Humano
    @property
    def inteligente(self):
        return True


if __name__ == '__main__':
    anonimo = Humano('Jhon Doe')

    try:
        anonimo.inteligente
    except NotImplementedError:
        print('Propriedade Abstrata')

    jose = HomoSapiens('José')
    print('{} da classe {}, inteligente: {}'.format(
        jose.nome, jose.__class__.__name__, jose.inteligente))

    grokn = Neanderthalensis('Grokn')
    print('{} da classe {}, inteligente: {}'.format(
        grokn.nome, grokn.__class__.__name__, grokn.inteligente))
