# contar y agregar elementos
unidades = ["Ibiza-01", "Bora-02", "VStar-03"]

print(f"Unidades al inicio: {len(unidades)}")

unidades.append("Versa-04")

print(f"Lista actualizada: {unidades}")
print(f"Unidades al final: {len(unidades)}")


#append y el in 
usuarios = ["jhair", "antonio", "fani"]
nuevo = "antonio"
if nuevo in usuarios:
    print("YA EXISTE ESE NOMBRE EN LA BD")
else:
    usuarios.append(nuevo)
    print("SE AGREGÓ CORRECTAMENTE")
print(f"BASE ACTUALIZADA: {usuarios}")  




servicios = ["Cambio de pasta", "Formateo PC", "Armado Gamer", "Limpieza"]

atendido = servicios.pop(0)
print(f"En proceso: {atendido}")

cancelado = servicios.pop()
print(f"Cancelado por el cliente: {cancelado}")

print(f"Quedan {len(servicios)} pendientes: {servicios}")
