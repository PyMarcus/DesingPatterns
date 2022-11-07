from content import MySQLFactory

"""
O Factory Method é um padrão criacional de projeto que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses
 alterem o tipo de objetos que serão criados.
"""

use_case = MySQLFactory.create()
print(use_case.do_something('dsa'))
