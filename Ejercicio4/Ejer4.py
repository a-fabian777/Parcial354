
"""
4. Con el uso de librerías en PYTHON, construya la dependencia de 
Abuelos, 
tios, 
padres, 
primos 
e hijos de su familia.
"""

from kanren import Relation, var, run, facts, eq

x = var()
y = var()
padre = Relation()
hermano = Relation()
facts(padre, 
      ('Raul', 'Esteban'), 
      ('Raul', 'Jose'), 
      ('Esteban', 'Andres'), 
      ('Esteban', 'Carlos'),
      ('Jose', 'Gladys')
      ('Jose', 'Marcelo')
      )
facts(hermano,
      ('Esteban', 'Jose'),
      ('Gladys', 'Marcelo'),
      ('Andres','Carlos')
      )


print(run(2,x,padre('Esteban',x)))
