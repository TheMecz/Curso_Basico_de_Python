nombre = input("¿Cuál es tu nombre?: ")

#La fución upper() convierte todo el texto en mayúsculas.
print (nombre.upper())

#La función capitalize() convierte la primera letra en mayúscula
#y las demás mantiene en minúsculas.
print (nombre.capitalize())

#La función strip() elimina los espacios basura que pueden estar al
#incio o al final de mi cadena de caracteres.
print (nombre.strip())

#La funcion lower() convierte todo el texto en minúsculas.
print(nombre.lower())

#La funcion replace() lo que hace es remplazar las letras o las palabras
#por otra que nosotros definamos.
print(nombre.replace('e','a'))

#La funcion len() nos permite saber el tamaño de nuestra cadena de caracteres.
print(len(nombre))


""" Una string es un cadena de caractere, entonces si defino mi variable nombre como:
    nombre = mecz_code
    Esto es lo que lee la consola:
    'm','e','c','z','_','c','o','d','e'
    
    Esto lo podemos representar como un arreglo:
    | m | e | c | z | _ | c | o | d | e |
      0   1   2   3   4   5   6   7   8    -> estos son los indices de posiones que tiene nuestro arreglo.
     -9  -8  -7  -6  -5  -4  -3  -2  -1    -> estos son los indices inversos de posicion que tiene nuestro arreglo.
    
    Entonces si colocamos:
    print(nombre[0])
    Nos imprimira:
    m
    """