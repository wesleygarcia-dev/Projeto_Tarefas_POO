from tarefa import Tarefa

class TarefaCasa(Tarefa):
    def __init__(self, titulo, descricao, comodo):
        super().__init__(titulo, descricao)
        self.comodo = comodo

    def tipo(self):
        return "Casa: " + self.comodo
