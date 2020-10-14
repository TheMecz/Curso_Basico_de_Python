"""El bucle while es una estructura de dato que nos permites repetir múltiples
tareas, siempre y cuando se cumpla la condición que le hayamos asignado."""
"""i = 1
while i < 100 :
    print(2 ** i)
    i += 1
"""
def run():
    Limite = 1000
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < Limite:
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador += 1
        potencia_2 = 2**contador

if __name__ == '__main__':
    run()

