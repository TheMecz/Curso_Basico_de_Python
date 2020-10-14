def run():
    palabra = input("Digite una palabra: ")
    i = 0
    while i < len(palabra):
        if palabra[i] == 'o':
            i += 1
            continue
        elif palabra[i] == 'a':
            break
        else:
            print(palabra[i])
            i += 1

if __name__ == '__main__':
    run()