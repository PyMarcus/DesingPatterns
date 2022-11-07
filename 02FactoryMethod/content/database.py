from .interface import DatabaseInterface
from typing import Dict


class MySQL(DatabaseInterface):
    """
    Usa a interface para ser obrigada
    a utilizar o método e reaproveitar o
    código, extendendo-a
    """
    def select(self) -> Dict:
        return {
            "status_code": 200
        }
