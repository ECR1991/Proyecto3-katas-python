# ============================
# EJERCICIO 13
# Mayúsculas y minúsculas de cada letra
# ============================

def mayus_minus(conjunto):
    return list(map(lambda letra: (letra.upper(), letra.lower()), conjunto))


# Prueba
print(mayus_minus({"a", "b", "c"}))
