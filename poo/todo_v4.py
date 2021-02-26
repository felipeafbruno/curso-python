from datetime import date, datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.lista_tarefas = []

    # __iter__ -> permite que agora a classe Projeto seja iteravel 
    # no caso a lista de tarefa
    def __iter__(self): 
        return self.lista_tarefas.__iter__()


    def add(self, descricao, vencimento=None):
        self.lista_tarefas.append(Tarefa(descricao, vencimento))


    def pendentes(self):
        return [tarefa for tarefa in self.lista_tarefas if not tarefa.feito]


    def procurar(self, descricao):
        # Possível IndexError
        return [tarefa for tarefa in self.lista_tarefas if tarefa.descricao == descricao][0]


    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluído)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dia(s))')

        return f'{self.descricao} ' + ' '.join(status)


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Brincar com o Bernardinho', datetime.now() + timedelta(days=1, minutes=12))
    casa.add('Brincar com a Furtuninha')
    casa.add('Terminar o módulo de POO', datetime.now())
    casa.add('Lavar os Pratos')

    casa.procurar('Lavar os Pratos').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')
        
    print(casa)

if __name__ == '__main__':
    main()
