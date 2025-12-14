# ============================
# EJERCICIO 2
# Dada una lista de números, obtener una nueva lista
# con el doble de cada valor usando map()
# ============================

def duplicar_numeros(lista):
    # Usamos map para multiplicar cada número por 2
    resultado = list(map(lambda numero: numero * 2, lista))

    # Devolvemos la nueva lista
    return resultado


# Prueba del ejercicio
numeros = [1, 2, 3, 4, 5]
resultado = duplicar_numeros(numeros)
print(resultado)
