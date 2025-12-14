# ============================
# EJERCICIO 12
# Devuelve la longitud de cada palabra
# ============================

def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))


# Prueba
print(longitud_palabras("hola mundo python"))
