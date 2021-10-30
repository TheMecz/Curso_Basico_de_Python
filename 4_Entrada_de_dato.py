"""Para almacenar un valor en una variable desde la entrada de teclado
utilizamos la función input."""

numero1 = input("Escribe un número: ")
numero2 = input("Escribe un número: ")
Suma = numero1 + numero2
print(Suma)

#Lo que aparece en consola es:
"""Escribe un número: 4"""
"""Escribe un número: 5"""
"""45"""
#Esto se debe a que estamos haciendo una suma de caracteres
#Para definir un entero desde la entra de teclado hacemos lo siguiente:

numero1 = int(input("Escribe un número: "))
numero2 = int(input("Escribe un número: "))
Suma = numero1 + numero2
print(Suma)

#Lo que aparece en consola es:
"""Escribe un número: 4"""
"""Escribe un número: 5"""
"""9"""
#Podemos hacer el mismo procedimiento para definir otro tipo de dato.
#Por ejemplo float, bool, entre otros.