from tarefa import Tarefa
from tarefa_estudo import TarefaEstudo
from tarefa_casa import TarefaCasa
from usuario import Usuario
from arquivo_tarefas import ArquivoTarefas

class Sistema:
    def __init__(self):
        self.usuario = Usuario("Aluno")
        self.arquivo = ArquivoTarefas()
        self.arquivo.carregar(self.usuario)
    def cadastrar(self):
        print("\n1 - Comum | 2 - Estudo | 3 - Casa")
        tipo = input("Tipo: ").strip()

        if tipo not in ("1", "2", "3"):
            print("Tipo invalido.")
            return

        titulo = input("Titulo: ").strip()

        if not titulo:
            print("O titulo nao pode estar vazio.")
            return

        descricao = input("Descricao: ").strip()

        if not descricao:
            print("A descricao nao pode estar vazia.")
            return

        if tipo == "2":
            materia = input("Materia: ").strip()

            if not materia:
                print("A materia nao pode estar vazia.")
                return

            tarefa = TarefaEstudo(titulo, descricao, materia)

        elif tipo == "3":
            comodo = input("Comodo: ").strip()

            if not comodo:
                print("O comodo nao pode estar vazio.")
                return

            tarefa = TarefaCasa(titulo, descricao, comodo)

        else:
            tarefa = Tarefa(titulo, descricao)

        self.usuario.adicionar_tarefa(tarefa)
        self.arquivo.salvar(self.usuario)

        print("Tarefa entendida!")
    
    def executar(self):
        while True:
            print("\n=== CONTROLE DE TAREFAS ===")
            print("1 - Cadastrar tarefa")
            print("2 - Listar tarefas")
            print("3 - Concluir tarefa")
            print("4 - Excluir tarefa")
            print("0 - Sair")
            opcao = input("Escolha: ").strip()
            if opcao == "1":
                self.cadastrar()
            elif opcao == "2":
                self.usuario.listar_tarefas()
            elif opcao in ("3", "4"):
                self.usuario.listar_tarefas()
                try:
                    numero = int(input("Numero da tarefa: "))
                except ValueError:
                    print("Digite um numero valido.")
                    continue
                if opcao == "3":
                    sucesso = self.usuario.concluir_tarefa(numero)
                else:
                    sucesso = self.usuario.excluir_tarefa(numero)
                if sucesso:
                    self.arquivo.salvar(self.usuario)
                    print("Operacao realizada!")
                else:
                    print("Tarefa nao encontrada.")
            elif opcao == "0":
                self.arquivo.salvar(self.usuario)
                print("Ate a Próxima Tarefa!")
                break
            else:
                print("essa opçao não deu irmão.")
