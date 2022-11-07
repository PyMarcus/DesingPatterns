from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    """
    Interface que contem metodo
    comum a todos objetos que serao
    apenas extendidos
    """
    @abstractmethod
    def select(self):
        ...
