# ============================
# EJERCICIO 16
# Palabras con más de n letras
# ============================

def palabras_largas(texto, n):
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))


# Prueba
print(palabras_largas("hola mundo python", 4))
