class Carro():
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0


    def acelerar(self, delta=5):
        self.velocidade_atual += delta
        return self.velocidade_atual if self.velocidade_atual < self.velocidade_maxima else self.velocidade_maxima


    def frear(self, delta=5):
        self.velocidade_atual -= delta
        return self.velocidade_atual if self.velocidade_atual >= 0  else 0


if __name__ == '__main__':
    carro1 = Carro(180)

    print('Acelerando...')
    for _ in range(25):
        print(carro1.acelerar(delta=8))

    print('Freando...')
    for _ in range(10):
        print(carro1.frear(20))
