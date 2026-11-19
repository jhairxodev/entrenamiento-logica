def clasificar_latencia_nodo(latencia_ms: float, activo: bool) -> str:
  
    if latencia_ms < 0:
        return "ERROR_TELEMETRIA"
    if not activo:
        return "NODO_OFFLINE"

    
    if latencia_ms >= 250.0:
        return "CRITICO"
    elif latencia_ms >= 100.0:
        return "DEGRADADO"
    else:
        return "OPTIMO"