menu1 =""":::SELECIONE ALGUNA DE NUESTRAS OPCIONES:::
1. Covertir alguna moneda a dolares.
2. Convertir dolares a alguna moneda.
3. Salir del programa.
"""

menu2 = """:::SELECCIONE ALGUNA DE NUESTRA OPCIONES:::
1. Convertir Nuevos Soles Peruanos a Dolares.
2. Convertir Pesos Colombianos a Dolares.
3. Convertir Pesos Mexicanos a Dolares.
4. Convertir Euros a Dolares.
5. Convertir Libras Esterlinas a Dolares.
"""
menu3 = """:::SELECCIONE ALGUNA DE NUESTRA OPCIONES:::
1. Convertir Dolares a Nuevos Soles.
2. Convertir Dolares a Pesos Colombianos.
3. Convertir Dolares a Pesos Mexicanos.
4. Convertir Dolares a Euros.
5. Convertir Dolares a Libras Esterlinas.
"""
menu4 = """:::Tipos de cambio:::
1. Un nuevo sol peruno esquivale a: 3.58.
2. Un peso colombiano esquivale a: 0.00026.
3. Un peso mexicano esquivale a: 0.047.
4. Un euro esquivale a: 1.18.
5. Una libra escarlina esquivale a: 1.30.
"""
def moneda_a_dolar(cambio):
    #Conversor de MONEDA a DOLAR
    moneda = float(input(":::Digite el monto a convertir: "))
    #El valor del dolar actualmente
    dolares = moneda / cambio
    print(":::El valor de " + str(moneda) + " en dolares es: " + str(dolares))

def dolar_a_moneda(cambio):
    #Conversor de DOLAR a MONEDA
    dolares = float(input(":::Digite el monto a convertir: "))
    #El valor del dolar actualmente
    moneda = dolares * cambio
    print(":::El valor de " + str(dolares) + " dolares es: " + str(moneda))

def imprimir_1():
    print(menu4)
    cambio = float(input(':::Digite el valor de cambio de la moneda: '))
    moneda_a_dolar(cambio)

def imprimir_2():
    print(menu4)
    cambio = float(input(':::Digite el valor de cambio de la moneda: '))
    dolar_a_moneda(cambio)

def monedas_a_dolares(opcion):
    if opcion == 1:
        imprimir_1()
    elif opcion == 2:
        imprimir_1()
    elif opcion == 3:
        imprimir_1()
    elif opcion == 4:
        imprimir_1()
    elif opcion == 5:
        imprimir_1()
    else:
        print("La opcion introducida no existe.")

def dolares_a_monedas(opcion):
    if opcion == 1:
        imprimir_2()
    elif opcion == 2:
        imprimir_2()
    elif opcion == 3:
        imprimir_2()
    elif opcion == 4:
        imprimir_2()
    elif opcion == 5:
        imprimir_2()
    else:
        print("La opcion introducida no existe.")

def resultado_1():
    print(menu2)
    opcion = int(input(":::Digite el número de la opción: "))
    monedas_a_dolares(opcion)

def resultado_2():
    print(menu2)
    opcion = int(input(":::Digite el número de la opción: "))
    dolares_a_monedas(opcion)



while True:
    print(":::Bienvenido al conversor de monedas 💰:::")
    print(menu1)
    opcion = int(input(":::Digite el número de la opción: "))
    if opcion == 1:
        resultado_1()
    elif opcion == 2:
        resultado_2()
    elif opcion == 3:
        print("Gracias por venir, vuelva pronto")
        break;
    else:
        print("La opción introducida no existe.")