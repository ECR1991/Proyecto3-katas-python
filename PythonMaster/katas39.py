# ============================
# EJERCICIO 39
# Calcular área de una figura
# ============================

def area_figura(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        radio = datos[0]
        return 3.1416 * radio * radio

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    else:
        return "Figura no válida"


# Pruebas
print(area_figura("rectangulo", (5, 3)))
print(area_figura("circulo", (2,)))
print(area_figura("triangulo", (10, 4)))
