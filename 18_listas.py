"""Una lista es una estructura de datos que nos permite almacenar diferentes
objetos dentro de un variable. Estos objetos pueden ser de diferente tipo."""

lista = [1,2,3,4,5,6]
print(lista)
#Obtenemos: [1, 2, 3, 4, 5, 6]

objetos = ['hola', 3, 4.5, True]
print(objetos)
#Obtenemos: ['hola', 3, 4.5, True]

#El método append("objeto") nos permite agregar un objeto al final de la lista.
objetos.append(False)
print(objetos)
#Obtenemos: ['hola', 3, 4.5, True, False]

#El método pop("índice") nos permite eliminar un objeto por medio de su índice.
objetos.pop(1)
print(objetos)
#Obtenemos: ['hola', 4.5, True, False]

#Tambien podemos recorrer una lista
for i in objetos:
    print(i)
#Obtenemos: 
# hola
#4.5
#True
#False

#Tambien podemos aplicar slices
print(objetos[1:3])
#Obtenemos: [4.5, True]

#Tambien podemos invertir una lista.
print(objetos[::-1])
#Obtenemos: [False, True, 4.5, 'hola']