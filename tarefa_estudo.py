from tarefa import Tarefa

class TarefaEstudo(Tarefa):
    def __init__(self, titulo, descricao, materia):
        super().__init__(titulo, descricao)
        self.materia = materia

    def tipo(self):
        return "Estudo: " + self.materia
