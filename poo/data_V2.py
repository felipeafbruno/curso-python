class Data:
    # O Pytho não permite mais de um construtor com em outras linguagens
    # para contornar isso é valid ousar parametro padrão
    # contrutor com paramentros
    def __init__(self, dia=1, mes=1, ano=1999):
        self.dia = dia
        self.mes = mes
        self.ano = ano 

    # todo o método de uma classe deve ter
    # obrigatoriamente self como parametro
    # self -> representa o objeto do contexto 
    # quando d1.to_str() o objeto do contexto/self é d1
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(mes=2,ano=2021)
print(d1)

d2 = Data(27,2,2021)
print(d2)
