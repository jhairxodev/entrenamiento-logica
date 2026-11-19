# Cuenta cuántas veces se superó el límite de 80 km/h (estrictamente mayor a 80).
velocidades: list[int] = [65, 85, 110, 70, 95, 80]
excesos: int = 0

for limite in velocidades:
    if limite > 80:
        excesos += 1
print("Cantidad de excesos de velocidad:", excesos)  # Debe imprimir 3


# Tienes $100 de saldo en el TAG y cada caseta cuesta $35.
# Objetivo: Mientras el saldo alcance para pagar una caseta (mayor o igual a 35),
# réstale 35 al saldo y suma 1 al contador de casetas cruzadas.
saldo_tag: int = 100
casetas_cruzadas: int = 0
while saldo_tag >= 35:
    saldo_tag -= 35
    casetas_cruzadas += 1

print("Casetas cruzadas:", casetas_cruzadas)  # Debe imprimir 2
print("Saldo sobrante:", saldo_tag)           # Debe imprimir 30