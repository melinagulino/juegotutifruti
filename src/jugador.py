class Jugador:
    def __init__(self, nombre):
        self.nombre_jugador = nombre

    def detectar_nombre_repetido(self, otro_jugador):
            return self.nombre_jugador.lower() == otro_jugador.nombre_jugador.lower()
