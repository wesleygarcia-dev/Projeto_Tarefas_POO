import json
from tarefa import Tarefa
from tarefa_estudo import TarefaEstudo
from tarefa_casa import TarefaCasa

class ArquivoTarefas:
    def __init__(self, caminho="tarefas.json"):
        self.__caminho = caminho  # Atributo privado

    def __transformar_em_dados(self, tarefa):  # Metodo privado
        dados = {"tipo": tarefa.tipo(), "titulo": tarefa.titulo,
                 "descricao": tarefa.descricao, "concluida": tarefa.esta_concluida()}
        if isinstance(tarefa, TarefaEstudo):
            dados["materia"] = tarefa.materia
            dados["classe"] = "estudo"
        elif isinstance(tarefa, TarefaCasa):
            dados["comodo"] = tarefa.comodo
            dados["classe"] = "casa"
        else:
            dados["classe"] = "comum"
        return dados

    def salvar(self, usuario):
        dados = {"nome": usuario.nome,
                 "tarefas": [self.__transformar_em_dados(t) for t in usuario.tarefas]}
        with open(self.__caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def carregar(self, usuario):
        try:
            with open(self.__caminho, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            return
        usuario.nome = dados.get("nome", usuario.nome)
        usuario.tarefas = []
        for item in dados.get("tarefas", []):
            classe = item.get("classe")
            titulo = item.get("titulo", "Sem titulo")
            descricao = item.get("descricao", "")
            if classe == "estudo":
                tarefa = TarefaEstudo(titulo, descricao, item.get("materia", ""))
            elif classe == "casa":
                tarefa = TarefaCasa(titulo, descricao, item.get("comodo", ""))
            else:
                tarefa = Tarefa(titulo, descricao)
            if item.get("concluida", False):
                tarefa.concluir()
            usuario.adicionar_tarefa(tarefa)
