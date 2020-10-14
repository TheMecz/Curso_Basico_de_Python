def divisores():
    contador = 0
    num = int(input('Digite un número: '))
    for i in range(1 ,num+1):
        if num % i == 0:
            contador += 1
    return contador
def es_primo():
    if divisores() > 2:
        print("El número no es primo.")
    else:
        print('El número es primo.')

if __name__ == '__main__':
    es_primo()