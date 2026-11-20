def evaluar_conexion(
    ip_origen: str,
    puerto: int,
    intentos_fallidos: int,
    es_red_interna: bool,
) -> str:
    # 1. Guard Clauses: validación de integridad del paquete
    if not (1 <= puerto <= 65535) or intentos_fallidos < 0:
        return "PAQUETE_INVALIDO"

    # 2. Lista negra con prioridad absoluta
    if ip_origen.startswith("185.220."):
        return "BLOQUEADO_LISTA_NEGRA"

    # 3. Mitigación de fuerza bruta (solo aplica a tráfico externo)
    if intentos_fallidos >= 5 and not es_red_interna:
        return "BLOQUEADO_FUERZA_BRUTA"

    # 4. Acceso administrativo interno
    if es_red_interna and puerto in {22, 5432}:
        return "PERMITIDO_ADMIN"

    # 5. Tráfico web estándar
    if puerto in {80, 443}:
        return "PERMITIDO_PUBLICO"

    # 6. Política Zero Trust por defecto
    return "DENEGADO_POR_DEFECTO"


if __name__ == "__main__":
    
    # Casos de prueba (si todos pasan, el script termina sin errores)
    assert evaluar_conexion("192.168.1.10", 0, 0, True) == "PAQUETE_INVALIDO"
    assert evaluar_conexion("185.220.101.4", 443, 0, True) == "BLOQUEADO_LISTA_NEGRA"
    assert evaluar_conexion("45.33.12.9", 22, 5, False) == "BLOQUEADO_FUERZA_BRUTA"
    assert evaluar_conexion("10.0.0.15", 22, 6, True) == "PERMITIDO_ADMIN"
    assert evaluar_conexion("201.140.22.1", 443, 2, False) == "PERMITIDO_PUBLICO"
    assert evaluar_conexion("10.0.0.15", 8080, 6, True) == "DENEGADO_POR_DEFECTO"

    print("Todas las reglas del firewall pasaron correctamente.")