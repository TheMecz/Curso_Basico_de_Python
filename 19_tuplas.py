"""Las tuplas son estructuras de datos estáticos porque no nos permite 
agregar o eliminar elementos dentro de la tupla, además a las tuplas se les
denomina por ser inmutables. """

mi_tupla = (1,2,3,4,5)
print(mi_tupla)
#Obtenemos: (1, 2, 3, 4, 5)

#La diferencia con las listas es que permite hacer recorridos más rápidos.
for numero in mi_tupla:
    print(numero)

