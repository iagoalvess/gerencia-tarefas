import unittest
from gerenciador import GerenciadorTarefas


class TestGerenciadorTarefas(unittest.TestCase):

    def setUp(self):
        self.gerenciador = GerenciadorTarefas()

    def test_adicionar_tarefa(self):
        self.gerenciador.adicionar_tarefa("Estudar Python")
        self.assertEqual(len(self.gerenciador.tarefas), 1)
        self.assertEqual(self.gerenciador.tarefas[0].descricao, "Estudar Python")
        self.assertFalse(self.gerenciador.tarefas[0].concluida)

    def test_adicionar_tarefa_duplicada(self):
        self.gerenciador.adicionar_tarefa("Fazer compras")
        with self.assertRaises(ValueError):
            self.gerenciador.adicionar_tarefa("Fazer compras")

    def test_marcar_tarefa_como_concluida(self):
        self.gerenciador.adicionar_tarefa("Ler um livro")
        sucesso = self.gerenciador.marcar_como_concluida("Ler um livro")
        self.assertTrue(sucesso)
        tarefa = self.gerenciador.buscar_tarefa("Ler um livro")
        self.assertTrue(tarefa.concluida)

    def test_marcar_tarefa_inexistente(self):
        sucesso = self.gerenciador.marcar_como_concluida("Dormir")
        self.assertFalse(sucesso)

    def test_listar_tarefas_pendentes(self):
        self.gerenciador.adicionar_tarefa("Tarefa 1")
        self.gerenciador.adicionar_tarefa("Tarefa 2")
        self.gerenciador.marcar_como_concluida("Tarefa 1")
        pendentes = self.gerenciador.listar_tarefas_pendentes()
        self.assertEqual(len(pendentes), 1)
        self.assertEqual(pendentes[0].descricao, "Tarefa 2")

    def test_listar_tarefas_concluidas(self):
        self.gerenciador.adicionar_tarefa("Tarefa 1")
        self.gerenciador.adicionar_tarefa("Tarefa 2")
        self.gerenciador.marcar_como_concluida("Tarefa 1")
        concluidas = self.gerenciador.listar_tarefas_concluidas()
        self.assertEqual(len(concluidas), 1)
        self.assertEqual(concluidas[0].descricao, "Tarefa 1")

    def test_remover_tarefa(self):
        self.gerenciador.adicionar_tarefa("Lavar o carro")
        self.assertEqual(len(self.gerenciador.tarefas), 1)
        sucesso = self.gerenciador.remover_tarefa("Lavar o carro")
        self.assertTrue(sucesso)
        self.assertEqual(len(self.gerenciador.tarefas), 0)


if __name__ == "__main__":
    unittest.main()
