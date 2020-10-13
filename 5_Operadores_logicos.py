#Existe 3 tipos de operadores lógicos

log1 = False
log2 = True

#El operador AND
print(log1 and log2)
#El resultado va a ser:
"""False"""
"""Esto pasa porque el operardor AND nos da True sólo 
cuando las dos variables son True."""

#El operador OR
print(log1 and log2)
#El resultado va a ser:
"""True"""
"""Esto pasa porque el operardor OR nos da False sólo 
cuando las dos variables son False."""

#El operador NOT
print(not log2)
#El resultado va a ser:
"""False"""
"""Esto pasa porque el operardor NOT contradice el valor 
lógico de una variable."""

#Tabla de verdad

""" |p|AND|q|  |Resultado|
    |T|   |F|  |    F    |
    |F|   |T|  |    F    |
    |F|   |F|  |    F    |
    |T|   |T|  |    T    |"""

""" |p|OR|q|  |Resultado|
    |T|  |F|  |    T    |
    |F|  |T|  |    T    |
    |F|  |F|  |    F    |
    |T|  |T|  |    T    |"""

"""  NOT|p|  |Resultado|
        |T|  |    F    |
        |F|  |    T    |"""