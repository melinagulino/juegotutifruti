import random
import string


class Tuttifruti:
    def __init__(self, cantidad_jugadores=2):
        self.letras_usadas = set()
        self.letra_actual = self.obtener_letra_aleatoria()
        self.cantidad_jugadores = cantidad_jugadores
        self.puntajes = {f"jugador{i + 1}": 0 for i in range(self.cantidad_jugadores)}
        self.jugadas = {f"jugador{i + 1}": {} for i in range(self.cantidad_jugadores)}
        self.valor_palabra_correcta = 10
        self.valor_palabra_repetida = 5
        self.valor_palabra_incorrecta = 0

    def obtener_letra_aleatoria(self):
        letras_disponibles = set(string.ascii_uppercase) - self.letras_usadas
        if not letras_disponibles:
            raise ValueError("Todas las letras han sido usadas.")
        letra = random.choice(list(letras_disponibles))
        self.letras_usadas.add(letra)
        return letra

    def validar_palabra(self, palabra):
        return bool(palabra) and palabra[0].upper() == self.letra_actual

    def _calcular_puntaje_jugador(self, palabra_jugador, palabras_oponente):
        total_puntos = 0
        if self.validar_palabra(palabra_jugador):
            if palabra_jugador not in palabras_oponente:
                 total_puntos += self.valor_palabra_correcta
            else:
                 total_puntos += self.valor_palabra_repetida
        else:
             total_puntos += self.valor_palabra_incorrecta
        return total_puntos

    def calcular_puntos(self):
        for i in range(self.cantidad_jugadores):
            jugador = f"jugador{i + 1}"
            palabras_jugador = {p.lower() for p in self.jugadas[jugador].values() if p}
            puntaje_total = self.puntajes.get(jugador, 0)


            palabras_oponente = set()
            for j in range(self.cantidad_jugadores):
                if i != j:
                    palabras_oponente.update({p.lower() for p in self.jugadas[f"jugador{j + 1}"].values() if p})

            for palabra_jugador in palabras_jugador:
                puntaje_total += self._calcular_puntaje_jugador(palabra_jugador, palabras_oponente)

            self.puntajes[jugador] = puntaje_total
        return self.puntajes

    def calcular_ganador(self):
        max_puntaje = max(self.puntajes.values())
        ganadores = [jugador for jugador, puntaje in self.puntajes.items() if puntaje == max_puntaje]

        if len(ganadores) > 1:
            return "Empate"
        else:
             ganador = ganadores[0]
             return f"Jugador {ganadores.index(ganador) + 1}"




