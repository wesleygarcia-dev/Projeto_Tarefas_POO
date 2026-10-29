class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []  

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
        for numero, tarefa in enumerate(self.tarefas, 1):
            print(f"{numero}. {tarefa.mostrar()}")

    def concluir_tarefa(self, numero):
        if 1 <= numero <= len(self.tarefas):
            self.tarefas[numero - 1].concluir()
            return True
        return False

    def excluir_tarefa(self, numero):
        if 1 <= numero <= len(self.tarefas):
            self.tarefas.pop(numero - 1)
            return True
        return False
