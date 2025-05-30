from src.tutifruti import Tuttifruti
from src.jugador import Jugador

class TuttifruttiControlador:
    def __init__(self, vista):
        self.vista = vista
        self.juego = Tuttifruti()

    def crear_jugador(self, nombre_jugador):
        try:
            self.juego.agregar_jugador(nombre_jugador)
        except ValueError as e:
            print(e)

    def obtener_jugadores(self):
        return list(self.juego.jugadores.keys())

    def manejar_jugada(self, jugador_id, palabra):
        self.juego.jugadas[jugador_id] = palabra
        puntajes = self.juego.calcular_puntos()
        self.vista.actualizar_puntajes(puntajes)

    def calcular_ganador(self):
        ganador = self.juego.calcular_ganador()
        if ganador:
            self.vista.mostrar_ganador(ganador.nombre_jugador)
        else:
            self.vista.mostrar_error("Es un empate.")

    def obtener_letra_actual(self):
        return self.juego.letra_actual
