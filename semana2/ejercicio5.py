# ==========================================
# APUNTES DE PYTHON: MANIPULACIÓN DE STRINGS
# ==========================================

# 1. Longitud de una cadena (len)
# Se usa para contar los caracteres de una palabra o texto.
palabra = "Python"
print(len(palabra))  # Imprime 6

# 2. Operadores de pertenencia (in / not in)
texto_base = "Programación en Python"
print("Python" in texto_base)    # Imprime True
print("Java" not in texto_base)  # Imprime True

# 3. Conversión a mayúsculas y minúsculas (.upper() y .lower())
texto = "Hola Mundo"
mayuscula = texto.upper()
minuscula = texto.lower()
print(mayuscula)   # "HOLA MUNDO"
print(minuscula)   # "hola mundo"

# 4. Quitar espacios en blanco (.strip())
# Elimina espacios sobrantes al inicio y al final de la cadena.
espacios = "   Hola con espacios   "
sinespacios = espacios.strip()
print(sinespacios)  # "Hola con espacios"

# 5. Indexación y Slicing (Rebanado)
# Los strings se indexan desde 0.
texto_slicing = "Este es un texto"
print(texto_slicing[2])       # Imprime 't' (caracter en el índice 2)
print(texto_slicing[0:3])     # Imprime 'Est' (desde 0 hasta antes del 3)
print(texto_slicing[:7])      # Imprime 'Este es' (desde el inicio hasta antes del 7)

# 6. Reemplazar texto (.replace())
# Cambia una subcadena por otra dentro del texto.
curso = "Este curso es de Javascript"
print(curso.replace("Javascript", "Python"))  # "Este curso es de Python"

# 7. Separar texto en listas (.split())
# Divide el string por espacios y lo convierte en una lista de palabras.
nuevo = curso.split()
print(nuevo)  # ['Este', 'curso', 'es', 'de', 'Javascript']

# 8. Normalización para búsquedas (case-insensitive)
# Convierte ambos a minúsculas para comparar sin importar las mayúsculas o minúsculas originales.
texto2 = "Este texto tiene MAYUSCULAS Y MINUSCULAS y necesito encontrar las palabras"
print("mayusculas".lower() in texto2.lower())  # Imprime True