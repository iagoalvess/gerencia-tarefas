from tarefa import Tarefa


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        if any(t.descricao == descricao for t in self.tarefas):
            raise ValueError("Tarefa com a mesma descrição já existe.")

        tarefa = Tarefa(descricao)
        self.tarefas.append(tarefa)
        return tarefa

    def buscar_tarefa(self, descricao):
        for tarefa in self.tarefas:
            if tarefa.descricao == descricao:
                return tarefa
        return None

    def marcar_como_concluida(self, descricao):
        tarefa = self.buscar_tarefa(descricao)
        if tarefa:
            tarefa.concluida = True
            return True
        return False

    def listar_tarefas_pendentes(self):
        return [t for t in self.tarefas if not t.concluida]

    def listar_tarefas_concluidas(self):
        return [t for t in self.tarefas if t.concluida]

    def remover_tarefa(self, descricao):
        tarefa = self.buscar_tarefa(descricao)
        if tarefa:
            self.tarefas.remove(tarefa)
            return True
        return False
