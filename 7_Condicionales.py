edad = int(input("Escribe tu edad: "))

#Las estructuras de datos condicionales nos ayudan a separar o predecir diferentes resultados.

"""IF es una estructura de dato que realiza una continuidad de nuestro programa
siempre y cuando se cumpla la condición."""
if edad > 0: #Lo que hace IF es preguntar: Si edad es mayor a 0 continua.

    if edad > 17: #Lo que hace IF es preguntar: Si edad es mayor a 17 continua.
        print("Es mayor de edad.")
    else: #Lo que hace es continuar si la condición en IF fue FALSE
        print("Es menor de edad.")

else: #Lo que hace es continuar si la condición en IF fue FALSE.
    print("El dato introducido es incorrecto.")

"""ELSE es una estructura de dato que nos ayuda a continuar el proceso de 
nuestro programa cuando la condición en nuestro IF nos da FALSE"""
#Los espacios realizados son denomiados identaciones y son obligatorios a la hora de programar en python
