# ============================
# EJERCICIO 30
# Determina si dos palabras son anagramas.
# ============================

def son_anagramas(palabra1, palabra2):
    # Pasamos a minúsculas para evitar problemas con mayúsculas
    p1 = palabra1.lower()
    p2 = palabra2.lower()

    # Si al ordenar las letras son iguales, son anagramas
    return sorted(p1) == sorted(p2)

# Prueba del ejercicio
print(son_anagramas("Roma", "Amor"))  # True
