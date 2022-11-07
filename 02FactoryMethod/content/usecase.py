from typing import Type, Dict, Union
from .interface import DatabaseInterface


class UseCase:
    def __init__(self, repository: Type[DatabaseInterface]):
        self.__repository = repository

    def do_something(self, data: bool) -> Union[Dict, None]:
        if data:
            response = self.__repository.select()
            return response
