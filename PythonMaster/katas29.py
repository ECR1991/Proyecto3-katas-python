# ============================
# EJERCICIO 29
# Enmascara todos los caracteres con '#' excepto los últimos cuatro.
# ============================

def enmascarar(variable):
    texto = str(variable)  # Convertimos a texto

    # Si tiene 4 o menos caracteres, no enmascaramos
    if len(texto) <= 4:
        return texto

    # Creamos tantos # como caracteres hay menos los 4 últimos
    return ("#" * (len(texto) - 4)) + texto[-4:]

# Prueba del ejercicio
print(enmascarar("123456789"))  # #####6789
