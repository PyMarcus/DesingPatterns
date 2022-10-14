from Singleton import Singleton


class App(metaclass=Singleton):
    """
    App herda da classe singular
    agora, so uma instancia é ,realmente,
    atribuida.Portanto, é impossível setar
    novos valores
    """
    def __init__(self, name_of_app: str) -> None:
        self.name_of_app = name_of_app

    def execute_something(self):
        print(f"Hi, this is {self.name_of_app}")


if __name__ == '__main__':
    app = App("joguin")
    app.execute_something()

    app2 = App("joguin2")  # nova instancia será joguin apenas, tambem.
    app2.execute_something()
