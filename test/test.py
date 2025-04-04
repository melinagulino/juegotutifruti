from src.tutifruti import Tuttifruti
from src.jugador import Jugador

def test_obtener_letra_aleatoria():
    juego = Tuttifruti()
    letra = juego.obtener_letra_aleatoria()

    assert letra.isalpha()
    assert len(letra) == 1

def test_validar_letra_que_no_sea_repetida():
    juego = Tuttifruti()
    primera_letra = juego.obtener_letra_aleatoria()
    segunda_letra = juego.obtener_letra_aleatoria()

    assert primera_letra != segunda_letra


def test_validar_palabra_ok():
    juego = Tuttifruti()
    juego.letra_actual = "M"

    assert juego.validar_palabra("Maria") is True
    assert juego.validar_palabra("Manzana") is True


def test_validar_palabra_no_ok():
    juego = Tuttifruti()
    juego.letra_actual = 'S'

    assert juego.validar_palabra("Maria") is False
    assert juego.validar_palabra("Juan") is False


def test_calcular_puntos():
    juego = Tuttifruti()
    juego.letra_actual = 'M'

    juego.jugadas["jugador1"] = {"nombre": "melina", "cosas": "mesa", "color": "marron"}
    juego.jugadas["jugador2"] = {"nombre": "maria", "cosas": "madera", "color": "morado"}

    juego.calcular_puntos()

    assert juego.puntajes["jugador1"] == 30
    assert juego.puntajes["jugador2"] == 30


def test_detectar_palabra_repetida():
    juego = Tuttifruti()
    juego.letra_actual = "D"
    juego.jugadas["jugador1"] = {"nombre": "Daniela", "cosas": "dedo", "color": "dorado"}
    juego.jugadas["jugador2"] = {"nombre": "Damian", "cosas": "diamante", "color": "dorado"}
    juego.calcular_puntos()

    assert juego.puntajes["jugador1"] == 25
    assert juego.puntajes["jugador2"] == 25

def test_validar_palabra_repetida_escrita_de_diferente_manera():
    juego = Tuttifruti()
    juego.letra_actual = "C"
    juego.jugadas["jugador1"] = {"nombre": "Carmen", "cosas": "CAsa", "color": "celeste"}
    juego.jugadas["jugador2"] = {"nombre": "Cesar", "cosas": "casa", "color": "colorado"}
    juego.calcular_puntos()

    assert juego.puntajes["jugador1"] == 25
    assert juego.puntajes["jugador2"] == 25

def test_calcular_palabra_incorrecta_con_casillero_vacio():
    juego = Tuttifruti()
    juego.letra_actual = "T"
    juego.jugadas["jugador1"] = {"nombre": "Tamara", "cosas": "tupper", "color": ""}
    juego.jugadas["jugador2"] = {"nombre": "Tomas", "cosas": "tarro", "color": "turqueza"}
    juego.calcular_puntos()

    assert juego.puntajes["jugador1"] == 20
    assert juego.puntajes["jugador2"] == 30


def test_calcular_ganador_del_juego():
    juego = Tuttifruti()
    juego.letra_actual = "M"
    juego.jugadas["jugador1"] = {"nombre": "melina", "cosas": "mesa", "color": "marron"}
    juego.jugadas["jugador2"] = {"nombre": "maria", "cosas": "madera", "color": "morado"}
    juego.calcular_puntos()

    juego.letra_actual = "A"
    juego.jugadas["jugador1"] = {"nombre": "Amanda", "cosas": "aro", "color": "amarillo"}
    juego.jugadas["jugador2"] = {"nombre": "Anibal", "cosas": "andador", "color": "azul"}
    juego.calcular_puntos()

    juego.letra_actual = "C"
    juego.jugadas["jugador1"] = {"nombre": "Camila", "cosas": "cama", "color": "colorado"}
    juego.jugadas["jugador2"] = {"nombre": "Cesar", "cosas": "corcho", "color": "celeste"}
    juego.calcular_puntos()

    assert juego.puntajes["jugador1"] == 90
    assert juego.puntajes["jugador2"] == 90
    assert juego.calcular_ganador() is None

    juego = Tuttifruti()
    juego.letra_actual = "M"
    juego.jugadas["jugador1"] = {"nombre": "melina", "cosas": "mesa", "color": "marron"}
    juego.jugadas["jugador2"] = {"nombre": "maria", "cosas": "madera", "color": "morado"}
    juego.calcular_puntos()

    juego.letra_actual = "A"
    juego.jugadas["jugador1"] = {"nombre": "Amanda", "cosas": "aro", "color": "amarillo"}
    juego.jugadas["jugador2"] = {"nombre": "Anibal", "cosas": "andador", "color": "azul"}
    juego.calcular_puntos()

    juego.letra_actual = "C"
    juego.jugadas["jugador1"] = {"nombre": "Camila", "cosas": "cama", "color": "colorado"}
    juego.jugadas["jugador2"] = {"nombre": "Cesar", "cosas": " ", "color": "celeste"}  # Casillero vacío
    juego.calcular_puntos()

    assert juego.puntajes["jugador1"] == 90
    assert juego.puntajes["jugador2"] == 80

    ganador = juego.calcular_ganador()
    assert ganador is not None
    assert ganador.nombre_jugador == "Melina"


def test_detectar_nombre_repetido():
    nombre_jugador1 = Jugador("Melina")
    nombre_jugador2 = Jugador("Melina")

    assert nombre_jugador1.detectar_nombre_repetido(nombre_jugador2) is True

    nombre_jugador1 = Jugador("Melina")
    nombre_jugador2 = Jugador("Melina1")

    assert nombre_jugador1.detectar_nombre_repetido(nombre_jugador2) is False
