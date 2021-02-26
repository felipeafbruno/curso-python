from datetime import date, datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.lista_tarefas = []

    # __iter__ -> permite que agora a classe Projeto seja iteravel
    # no caso a lista de tarefa
    def __iter__(self):
        return self.lista_tarefas.__iter__()

    # "método privado" '_' é uma conveção do python que indica que um método
    #só pode ser acessado dentra da prórpia classe
    def _add_tarefa(self, tarefa, **kwargs):
        self.lista_tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.lista_tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        # verificando se tarefa é uma instancia de Tarefa ou se é uma descricao
        # assim correta é ecolhida e os parametros são passados
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

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


# Esse ponto diz que a classe Tarefa é a super classe de TarefaRecorrente
class TarefaRecorrente(Tarefa): # HERANÇA
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias           

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento)

def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Brincar com o Bernardinho', datetime.now() +
             timedelta(days=1, minutes=12))
    casa.add('Brincar com a Furtuninha')
    casa.add('Terminar o módulo de POO', datetime.now())
    casa.add('Lavar os Pratos')
    casa.add(TarefaRecorrente('Trocar lençóis', datetime.now(), 7))
    casa.add(casa.procurar('Trocar lençóis').concluir())
    casa.procurar('Lavar os Pratos').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')

    print(casa)


if __name__ == '__main__':
    main()
