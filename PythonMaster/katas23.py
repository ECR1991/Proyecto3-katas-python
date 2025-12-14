# ============================
# EJERCICIO 23
# Concatena una lista de palabras. Usa la función reduce().
# ============================

from functools import reduce

def concatenar_palabras(lista):
    # Vamos juntando palabra a palabra con un espacio
    return reduce(lambda a, b: a + " " + b, lista)

# Prueba del ejercicio
print(concatenar_palabras(["Hola", "mundo", "Python"]))  # "Hola mundo Python"
