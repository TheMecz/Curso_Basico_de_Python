nombre = "mecz_code"

#Partición de cadenas de caracteres.
#Podemos 
print(nombre[0:4]) 
#Obtenemos: mecz

#Podemos hacer particiones desde el inicio hasta un valor antes.
print(nombre[:4]) 
#Obtenemos: mecz

#Poder hacer particiones desde el final hasta una determianda posición.
print(nombre[0:])
#Obtenemos: mecz_code

#Podemos hacer particiones desde un número hasta otro, pero realizando
#un determinado números de salto.
print(nombre[1:9:2])
#Obtenemos: ezcd

#Podemos mostrar el nombre completo
print(nombre[::])
#Obtenemos: mecz_code

#Podemos mostrar el nombre al reves
print(nombre[::-1])
#Obtenemos: edoc_zcem