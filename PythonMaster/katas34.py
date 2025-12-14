# ============================
# EJERCICIO 34
# Clase Arbol
# ============================

class Arbol:
    def __init__(self):
        # El tronco empieza con longitud 1
        self.tronco = 1
        # La lista de ramas empieza vacía
        self.ramas = []

    def crecer_tronco(self):
        # Aumenta el tronco en 1
        self.tronco += 1

    def nueva_rama(self):
        # Añade una rama con longitud 1
        self.ramas.append(1)

    def crecer_ramas(self):
        # Aumenta en 1 la longitud de cada rama
        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    def quitar_rama(self, posicion):
        # Quita la rama según la posición (empezando en 1)
        if posicion >= 1 and posicion <= len(self.ramas):
            self.ramas.pop(posicion - 1)
        else:
            print("Posición de rama no válida")

    def info_arbol(self):
        # Devuelve la información del árbol
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }


# ============================
# Caso de uso (paso a paso)
# ============================

# a. Crear un árbol
arbol = Arbol()

# b. Hacer crecer el tronco una unidad
arbol.crecer_tronco()

# c. Añadir una nueva rama
arbol.nueva_rama()

# d. Hacer crecer todas las ramas una unidad
arbol.crecer_ramas()

# e. Añadir dos nuevas ramas
arbol.nueva_rama()
arbol.nueva_rama()

# f. Retirar la rama situada en la posición 2
arbol.quitar_rama(2)

# g. Obtener información sobre el árbol
print(arbol.info_arbol())
