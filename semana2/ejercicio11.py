"""
Práctica: Estructuras de control repetitivas (for y while) con condicionales.
"""

# ==============================================================================
# EJERCICIO 1: Bucle FOR — Auditoría de Ingresos en Flota
# ==============================================================================
tarifas_viajes: list[float] = [48.5, 135.0, 62.0, 210.0, 39.0, 150.0]
viajes_altos: int = 0
ingreso_viajes_altos: float = 0.0

for tarifa in tarifas_viajes:
    if tarifa > 100.0:
        viajes_altos += 1
        ingreso_viajes_altos += tarifa

print("--- Ejercicio 1: Auditoría de Ingresos ---")
print(f"Cantidad de viajes altos: {viajes_altos}")
print(f"Ingreso total por viajes altos: {ingreso_viajes_altos}\n")


# ==============================================================================
# EJERCICIO 2: Bucle WHILE — Transferencia de Respaldo en Red
# ==============================================================================
archivo_restante_mb: int = 500
velocidad_por_segundo_mb: int = 120
segundos_totales: int = 0

print("--- Ejercicio 2: Transferencia en Red ---")
while archivo_restante_mb > 0:
    archivo_restante_mb -= velocidad_por_segundo_mb
    segundos_totales += 1

    if archivo_restante_mb < 0:
        archivo_restante_mb = 0

    print(f"Restante: {archivo_restante_mb} MB")

print(f"Tiempo total: {segundos_totales} segundos\n")


# ==============================================================================
# EJERCICIO 3: Bucle FOR + IF/ELSE — Clasificación de Turno
# ==============================================================================
ganancias_turno: list[float] = [45.0, 110.0, 85.0, 32.5, 140.0, 60.0]
viajes_buenos: int = 0
viajes_bajos: int = 0

for monto in ganancias_turno:
    if monto >= 80.0:
        viajes_buenos += 1
    else:
        viajes_bajos += 1

print("--- Ejercicio 3: Clasificación de Turno ---")
print(f"Total de viajes buenos: {viajes_buenos}")
print(f"Total de viajes bajos: {viajes_bajos}\n")


# ==============================================================================
# EJERCICIO 4: Bucle WHILE — Meta Diaria de Ingresos
# ==============================================================================
dinero_acumulado: int = 0
pago_por_viaje: int = 65
meta_diaria: int = 300
viajes_realizados: int = 0

while dinero_acumulado < meta_diaria:
    dinero_acumulado += pago_por_viaje
    viajes_realizados += 1

print("--- Ejercicio 4: Meta Diaria ---")
print(f"Viajes necesarios para la meta: {viajes_realizados}")
print(f"Dinero total acumulado: {dinero_acumulado}")