# EJERCICIO 3: Sumar los dígitos de un número usando un ciclo while y acumulador
# Ejemplo: 1234 -> 1 + 2 + 3 + 4 = 10

numero= 1234
suma = 0
while numero > 0:
    suma += numero % 10
    numero //= 10
    print (f"La suma de los digitos es: {suma}")