#Agregar una funcion
def es_mayor_de_edad(edad: int) -> bool:
    if edad >= 18:
        return True    # Si tiene 18 o más, regresa True
    else:
        return False   # Si tiene menos de 18, regresa False

prueba = es_mayor_de_edad(20)
print (prueba)   