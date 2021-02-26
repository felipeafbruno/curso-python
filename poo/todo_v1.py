from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + ('(Concluída)' if self.feito else '')


def main():
    casa = []
    casa.append(Tarefa('Terminar o módulo de POO'))
    casa.append(Tarefa('Brincar com o Benado :)'))
    casa.append(Tarefa('Brincar dom a Futuna :)'))
    casa.append(Tarefa('Lavar Prato'))

    # Minha Solução para cocluir a tarefa 'Lavar Prato'
    for tarefa in casa:
        if tarefa.descricao == 'Lavar Prato':
            tarefa.concluir()

    # As comprehension não são apenas para criar listas, dicionarios... :)
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar Prato']

    print(casa[3])
 
if __name__ == '__main__':
    main()
