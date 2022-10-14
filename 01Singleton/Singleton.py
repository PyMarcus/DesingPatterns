class Singleton(type):
    """
    O padrão singleton é usado
    quando se precisa, em todo o projeto,
    ter apenas uma unica instância da classe,
    isto é, um objeto.

    Pelo fato de não utilizar o operador new
    e ser construído em cima de métodos
    estáticos, essencialmente, ele faz apenas
    uma única referência à memória, isto é,para
    um único local

    No diagrama UML, a própria classe se referencia
    (um retangulo com uma seta que sai dele e volta para
    ele)

    Na prática, é muito usado quando se quer acessar
    um arquivo compartilhado
    """
    __instances = {}                                          # atributo privado

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:                          # verifica se já foi instanciada
            instance = super().__call__(*args, **kwargs)      # cria instancia da propria classe
            cls.__instances[cls] = instance                   # armazena instancia na memória
        return cls.__instances[cls]                           # retorna a instancia




