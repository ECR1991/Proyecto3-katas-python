# ============================
# EJERCICIO 27
# Crea una función que calcule el promedio de una lista de números.
# ============================

def promedio(lista):
    # Sumamos todo y dividimos entre la cantidad de números
    return sum(lista) / len(lista)

# Prueba del ejercicio
print(promedio([10, 20, 30]))  # 20.0
