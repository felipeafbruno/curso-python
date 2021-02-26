from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.lista_tarefas = []

    def add(self, descricao):
        self.lista_tarefas.append(Tarefa(descricao))


    def pendentes(self):
        return [tarefa for tarefa in self.lista_tarefas if not tarefa.feito]


    def procurar(self, descricao):
        # Possível IndexError
        return [tarefa for tarefa in self.lista_tarefas if tarefa.descricao == descricao][0]


    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


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
    casa = Projeto('Tarefas de Casa')
    casa.add('Brincar com o Bernardinho')
    casa.add('Brincar com a Furtuninha')
    casa.add('Terminar o módulo de POO')
    casa.add('Lavar os Pratos')

    casa.procurar('Lavar os Pratos').concluir()
    for tarefa in casa.lista_tarefas:
        print(f'{tarefa}')
        
    print(tarefa)

if __name__ == '__main__':
    main()
