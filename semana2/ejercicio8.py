#De "192.168.1.10" saca los 4 octetos como enteros y valida que cada uno vaya de 0 a 255

ip = "192.168.1.10"

# 1. Separamos el texto por los puntos y convertimos cada parte a entero
partes = ip.split(".")
octetos = []

for parte in partes:
    octetos.append(int(parte))

# 2. Validamos que cada octeto esté en el rango de 0 a 255
valido = True
for octeto in octetos:
    if not (0 <= octeto <= 255):
        valido = False
        break # Si uno falla, rompemos el ciclo porque ya no es válida

# Imprimimos resultados para ver que funcione
print(f"Los octetos como enteros son: {octetos}")

if valido:
    print("¡Validación exitosa! Todos los octetos están entre 0 y 255.")
else:
    print("Alerta: Hay un octeto fuera del rango permitido.")