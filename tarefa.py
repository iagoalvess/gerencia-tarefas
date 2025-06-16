class Tarefa:
    def __init__(self, descricao):
        if not descricao or not isinstance(descricao, str):
            raise ValueError("A descrição não pode ser vazia.")
        self.descricao = descricao
        self.concluida = False

    def __str__(self):
        status = "✓" if self.concluida else " "
        return f"[{status}] {self.descricao}"
