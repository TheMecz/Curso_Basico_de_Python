import random

def generar_password():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    simbolos = ['!', '¡', '¿', '?', '#', '$', '&', '%', '/', '=', '_', '-', '+', '{', '}', '[', ']']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    caracteres = mayusculas + minusculas + simbolos + numeros
    password = []
    for i in range(15):
        #Lo que hace choice es escoger un caracter random de nuestra lista de caracteres.
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    #Esta es una forma de convertir una lista en una cadena de caracteres.
    password = ''.join(password)
    return password

def run():
    password = generar_password()
    print('Tu nueva contraseña es: ' + password)

if __name__ == '__main__':
    run()