class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.__concluida = False

    def concluir(self):
        self.__concluida = True

    def esta_concluida(self):
        return self.__concluida

    def tipo(self):
        return "Comum"

    def mostrar(self):
        situacao = "Concluida" 
        if self.__concluida 
            else "Pendente"
        return f"[{situacao}] {self.titulo} - {self.descricao} ({self.tipo()})"
