# ============================
# EJERCICIO 5
# Calcula la media y devuelve si está aprobado o suspenso
# ============================

def calcular_media(lista, nota_aprobado=5):
    media = sum(lista) / len(lista)

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return media, estado


# Prueba
print(calcular_media([6, 7, 5]))
