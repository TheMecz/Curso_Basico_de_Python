def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        return True
    else:
        return False
    
def run():
    palabra = input("Digite una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("El palabra es palíndroma.")
    else:
        print("La palabra no es palíndroma.")

if __name__ == '__main__':
    run()