# ============================
# EJERCICIO 28
# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
# ============================

def primer_duplicado(lista):
    vistos = []

    for elemento in lista:
        # Si ya lo vimos antes, es el primer duplicado
        if elemento in vistos:
            return elemento
        # Si no, lo guardamos
        vistos.append(elemento)

    # Si no hay duplicados
    return None

# Prueba del ejercicio
print(primer_duplicado([1, 2, 3, 2, 4]))  # 2
