menu1 =""":::SELECIONE ALGUNA DE NUESTRAS OPCIONES:::
1. Covertir alguna moneda a dolares.
2. Convertir dolares a alguna moneda."""

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
print(":::Bienvenido al conversor de monedas 💰:::")
print(menu1)
opcion = int(input(":::Digite el número de la opción: "))
if opcion == 1:

    print(menu2)
    opcion = int(input(":::Digite el número de la opción: "))
    if opcion == 1:
        #Conversor de NUEVOS SOLES PERUANOS a DOLAR
        moneda = float(input(":::Digite el monto a convertir: "))
        #El valor del dolar actualmente
        cambio = 3.58
        dolares = moneda / cambio
        print(":::El valor de " + str(moneda) + " soles en dolares es: " + str(dolares))
    
    elif opcion == 2:
        #Converso de Pesos Colombianos a DOLAR
        moneda = float(input(":::Digite el monto a convertir: "))
        #El valor del dolar actualmente
        cambio = 0.00026
        dolares = moneda / cambio
        print(":::El valor de " + str(moneda) + " pesos colombianos en dolares es: " + str(dolares))
    elif opcion == 3:    
        #Converso de Pesos Mexiacanos a DOLAR
        moneda = float(input(":::Digite el monto a convertir: "))
        #El valor del dolar actualmente
        cambio = 0.047
        dolares = moneda / cambio
        print(":::El valor de " + str(moneda) + " pesos mexicanos en dolares es: " + str(dolares))
    elif opcion == 4:
        #Converso de EUROS a DOLAR
        moneda = float(input(":::Digite el monto a convertir: "))
        #El valor del dolar actualmente
        cambio = 1.18
        dolares = moneda / cambio
        print(":::El valor de " + str(moneda) + " euros en dolares es: " + str(dolares))
    elif opcion == 5:
        #Converso de Libras Escarlinas a DOLAR
        moneda = float(input(":::Digite el monto a convertir: "))
        #El valor del dolar actualmente
        cambio = 1.30
        dolares = moneda / cambio
        print(":::El valor de " + str(moneda) + " libras escarlinas en dolares es: " + str(dolares))
    else:
        print("La opcion introducida no existe.")
        
elif opcion == 2:
    
    print(menu3)
    opcion = int(input("Digite el número de la opción: "))
    if opcion == 1:
        #Conversor de DOLAR a NUEVOS SOLES PERUANOS
        dolares = float(input(":::Digite el monto a convertir: "))
        #El valor del dolar actualmente
        cambio = 3.58
        moneda = dolares * cambio
        print(":::El valor de " + str(dolares) + " dolares es: " + str(moneda))
        
    elif opcion == 2:
        #Converso de Pesos Colombianos a DOLAR
        dolares = float(input(":::Digite el monto a convertir: "))
        #El valor del dolar actualmente
        cambio = 0.00026
        moneda = dolares * cambio
        print(":::El valor de " + str(dolares) + " dolares es: " + str(moneda))
    elif opcion == 3:
        #Converso de Pesos Mexiacanos a DOLAR
        dolares = float(input(":::Digite el monto a convertir: "))
        #El valor del dolar actualmente
        cambio = 0.047
        moneda = dolares * cambio
        print(":::El valor de " + str(dolares) + " dolares es: " + str(moneda))
    elif opcion == 4:
        #Converso de EUROS a DOLAR
        dolares = float(input(":::Digite el monto a convertir: "))
        #El valor del dolar actualmente
        cambio = 1.18
        moneda = dolares * cambio
        print(":::El valor de " + str(dolares) + " dolares es: " + str(moneda))
    elif opcion == 5:
        #Converso de Libras Escarlinas a DOLAR
        dolares = float(input(":::Digite el monto a convertir: "))
        #El valor del dolar actualmente
        cambio = 1.30
        moneda = dolares * cambio
        print(":::El valor de " + str(dolares) + " dolares es: " + str(moneda))
    else:
        print("La opcion introducida no existe.")
    
else:
    print("La opción introducida no existe.")