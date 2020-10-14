"""Los diccionarios son estructuras de datos de llaves y valores.
Las llaves no son números que van de 0 a n, entonces no vamos a poder acceder a 
ellas por medio los índices. En este caso para acceder a un elemento es por medio 
de sus llaves. Una forma de entender estas llaves es imaginas que son el nombre de sus índices."""

def run():
    diccionario = {'key1': 1, 'key2' : 2, 'key3': 3}
    print(diccionario)

if __name__ == '__main__':
    run()

# Obtemos: {'key1': 1, 'key2': 2, 'key3': 3}

def run():
    diccionario = {'key1': 1, 'key2' : 2, 'key3': 3}
    print(diccionario['key1'])
    print(diccionario['key2'])
    print(diccionario['key3'])
    
if __name__ == '__main__':
    run()
# Obtemos:
# 1
# 2
# 3

def run():
    poblacion_paises = {'Argentina': 44938712, 'Brasil' : 210147125, 'Colombia': 50372424}
    print(poblacion_paises['Argentina'])
    print(poblacion_paises['Brasil'])
    print(poblacion_paises['Colombia'])
    
if __name__ == '__main__':
    run()
# Obtenemos:
# 44938712
# 210147125
# 50372424

def run():
    poblacion_paises = {'Argentina': 44938712, 'Brasil' : 210147125, 'Colombia': 50372424}
    #Este método nos ayuda a mostrar el nombre de las llaves de nuestro diccionario.
    for pais in poblacion_paises.keys():
        print(pais)
    
if __name__ == '__main__':
    run()
# Obtenemos:
# Argentina
# Brasil
# Colombia

def run():
    poblacion_paises = {'Argentina': 44938712, 'Brasil' : 210147125, 'Colombia': 50372424}
    #Este método nos ayuda a mostrar los valores del diccionario.
    for pais in poblacion_paises.values():
        print(pais)
    
if __name__ == '__main__':
    run()
# Obtenemos:
# 44938712
# 210147125
# 50372424

def run():
    poblacion_paises = {'Argentina': 44938712, 'Brasil' : 210147125, 'Colombia': 50372424}
    #Este método nos ayuda a mostrar los dos valores del diccionario. Las llaves y el valor en esa llave.
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')
    
if __name__ == '__main__':
    run()
# Obtenemos:
# Argentina tiene 44938712 habitantes
# Brasil tiene 210147125 habitantes
# Colombia tiene 50372424 habitantes