from content import MySQLFactory


use_case = MySQLFactory.create()
print(use_case.do_something('dsa'))
