# LÓGICA: clasificar(n: int) -> str 
# Hacer una función que devuelva un string indicando si el número es:
# - Par o impar
# - Positivo, negativo o cero
# Nota: La función solo calcula y regresa el resultado; el input() y el print() van afuera.

print ("EJERCICIO 4 DE LA SEMAN 2")
#primero voy a hacer una funcion
def clasificar(n: int) ->str:
    #DEFINIR SI ES PAR O IMPAR
    if n % 2 == 0:
        par_impar = "PAR"
    else:
        par_impar = "IMPAR"

    #DEFINIR SI ES POSITIVO O NEGATIVO 
    if n > 0:
        positivo_negativo = "POSITIVO"
    elif n < 0:
        positivo_negativo = "NEGATIVO"
    else:
        positivo_negativo ="CERO"
    return f"El número es {par_impar} y {positivo_negativo}"

#DESPUES DE DEFINIR VAMOS CON LO SIGUIENTE
numero = int (input("INGRESA TU NUMERO ENTERO (Ejemplo: 5, 10, 400): "))
resultado = clasificar (numero)
print (resultado)
