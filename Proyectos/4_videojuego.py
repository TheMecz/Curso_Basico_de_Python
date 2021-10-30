import random

def run():
    num_random = random.randint(1, 100)
    num_elegido = int(input('Elige un número del 1 al 100: '))
    vidas = 5
    if vidas > 0:
        while num_random != num_elegido:
            if vidas == 0:
                break
            elif num_elegido < num_random:
                print('Piensa en un número más grande')
            else:
                print('Piensa en un número más pequeño')
            vidas -= 1
            print('Te quedan ' + str(vidas) + ' vidas ♥')
            num_elegido = int(input('Elige un número del 1 al 100: '))
        print('¡FELICIDADES! tú número coincide con el número seleccionado por la computadora 😃')
    else:
        print("¡Game Over!")

if __name__ == '__main__':
    run()
