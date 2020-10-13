#Conversor de un NUEVO SOL PERUANO a DOLAR
print(":::Bienvenido a nuestro conversor de Soles a Dolares:::")
soles = float(input(":::Digite el monto a convertir: "))

#El valor del dolar actualmente
cambio = 3.58

dolares = soles / cambio

print(":::El valor de " + str(soles) + " soles en dolares es: " + str(dolares))

#Conversor de DOLAR a NUEVO SOL PERUANO
print(":::Bienvenido a nuestro conversor de Dolares a Soles:::")
dolares = float(input(":::Digite el monto a convertir: "))

#El valor del dolar actualmente
cambio = 3.58

soles = dolares * cambio

print(":::El valor de " + str(dolares) + " dolares en soles es: " + str(soles))