from .usecase import UseCase
from .database import MySQL


class MySQLFactory:
    """
    Classe que cria os objetos
    com o tipo selecionado
    se precisar alterar, basta trocar a instancia

    """
    @staticmethod
    def create() -> UseCase:
        return UseCase(MySQL())  # retorna o objeto criado com a dependencia do mysql