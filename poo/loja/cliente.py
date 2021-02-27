from loja.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        if len(self.compras) > 0:
            data = self.compras[-1].data
            return data

    def total_compras(self):
        total = 0
        if len(self.compras):
            for compra in self.compras:
                total += compra.valor
        return total