from sistema import Sistema
from tarefa import Tarefa

if __name__ == "__main__":
    
    sistema = Sistema()
    exemplo = Tarefa("Exemplo", "Objeto de demonstracao")
    sistema.executar()
