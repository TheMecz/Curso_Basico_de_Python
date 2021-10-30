"""Cunado tratamos de repetir lineas o bloques de código nuestro programa puede volverce
muy extenso, entonces lo que hacemos es crear una función que nos ayude a realizar
este proceso en una sola linea de código."""

print('Mensaje especial: ')
print('¡Estoy aprendiendo a usar funciones!')
print('Mensaje especial: ')
print('¡Estoy aprendiendo a usar funciones!')
print('Mensaje especial: ')
print('¡Estoy aprendiendo a usar funciones!')

#De esta manera definimos una función

def imprimir():
    print('Mensaje especial: ')
    print('¡Estoy aprendiendo a usar funciones!')

#De esta manera podemos llamar a la función.
#Tambien obtenemos el mismo resultado que al inicio.

imprimir()
imprimir()
imprimir()

def conversacion(mensaje):
    print('Hola')
    print('¿Cómo estás?')
    print(mensaje)
    print('Adios')

opcion = int(input('Elige una opción (1, 2, 3): '))
if opcion == 1:
    conversacion('Elegiste la opción 1')
elif opcion == 2:
    conversacion('Elegiste la opción 2')
elif opcion == 3:
    conversacion('Elegiste la opción 3')
else:
    print('Escribe la opción correcta')