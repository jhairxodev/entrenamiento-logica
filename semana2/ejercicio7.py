#CONTAR LAS VOCALES DE UNA FRASE CON UN ACUMULADOR Y SUMAR 1 POR VOCAL

palabra = input("INGRESA TU PALABRA: ")
contador = 0
for letra in palabra:
    if letra in "aeiouáéíóú":
        contador += 1
print(f"El total de vocales es: {contador}")