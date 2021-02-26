class Data:
    # todo o método de uma classe deve ter
    # obrigatoriamente self como parametro
    # self -> representa o objeto do contexto 
    # quando d1.to_str() o objeto do contexto/self é d1
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 26
d1.mes = 2
d1.ano = 2021
print(d1)

d2 = Data()
d2.dia = 27
d2.mes = 2
d2.ano = 2021
print(d2)
