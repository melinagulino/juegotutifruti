from src.tutifruti import Tuttifruti

def test_obtener_letra_aleatoria():
    juego = Tuttifruti()
    letra = juego.obtener_letra_aleatoria()

    print(letra)
    assert letra.isalpha()

def test_validar_palabra_ok():
    juego = Tuttifruti()
    juego.letra_actual = "M"
    palabra = "Maria"
    resultado =  juego.validar_palabra(palabra)

    assert resultado == True

    juego = Tuttifruti()
    juego.letra_actual = "N"
    palabra = "Nadia"
    resultado = juego.validar_palabra(palabra)

    assert resultado == True

def test_validar_palabra_no_ok():
    juego = Tuttifruti()
    juego.letra_actual = 'S'
    palabra = "Maria"
    resultado =  juego.validar_palabra(palabra)

    assert resultado == False

    juego = Tuttifruti()
    juego.letra_actual = 'D'
    palabra = "Juan"
    resultado = juego.validar_palabra(palabra)

    assert resultado == False

def test_calcular_puntos():
    juego = Tuttifruti()
    juego.letra_actual = 'M'
    juego.jugada_jugador1= {"nombre": "melina", "cosas": "mesa" , "color": "marron"}
    juego.jugada_jugador2 = {"nombre": "maria", "cosas" : "madera", "color" : "morado"}
    juego.calcular_puntos()

    assert juego.total_jugador1 == 30
    assert juego.total_jugador2 == 30

    juego = Tuttifruti()
    juego.letra_actual = 'A'
    juego.jugada_jugador1 = {"nombre": "Amanda", "cosas": "aro", "color": "amarillo"}
    juego.jugada_jugador2 = {"nombre": "Anibal", "cosas": "andador", "color": "azul"}
    juego.calcular_puntos()

    assert juego.total_jugador1 == 30
    assert juego.total_jugador2 == 30

def test_detectar_palabra_repetida():
    juego = Tuttifruti()
    juego.letra_actual = "D"
    juego.jugada_jugador1 = {"nombre": "Daniela", "cosas": "dedo", "color": "dorado"}
    juego.jugada_jugador2 = {"nombre": "Damian", "cosas": "diamante", "color": "dorado"}
    juego.calcular_puntos()

    assert juego.total_jugador1 == 25
    assert juego.total_jugador2 == 25

def test_validar_palabra_repetida_escrita_de_diferente_manera():
    juego = Tuttifruti()
    juego.letra_actual = "C"
    juego.jugada_jugador1 = {"nombre": "Carmen", "cosas": "CAsa", "color": "celeste"}
    juego.jugada_jugador2 = {"nombre": "Cesar", "cosas": "casa", "color": "colorado"}
    juego.calcular_puntos()

    assert juego.total_jugador1 == 25
    assert juego.total_jugador2 == 25

def calcular_palabra_incorrecta_con_casillero_vacio():
    juego = Tuttifruti()
    juego.letra_actual = "T"
    juego.jugada_jugador1 = {"nombre": "Tamara", "cosas": "tupper", "color": ""}
    juego.jugada_jugador2 = {"nombre": "Tomas", "cosas": "tarro", "color": "turqueza"}
    juego.calcular_puntos()

    assert juego.total_jugador1 == 20
    assert juego.total_jugador2 == 30

def calcular_palabra_incorrecta_con_casillero_mal_escrito():
    juego = Tuttifruti()
    juego.letra_actual = "T"
    juego.jugada_jugador1 = {"nombre": "Tamara", "cosas": "tupper", "color": "turqeza"}
    juego.jugada_jugador2 = {"nombre": "Tomas", "cosas": "tarro", "color": "turqueza"}
    juego.calcular_puntos()

    assert juego.total_jugador1 == 20
    assert juego.total_jugador2 == 30

def test_calcular_ganador_del_juego():
    juego = Tuttifruti()
    juego.letra_actual = "M"
    juego.jugada_jugador1 = {"nombre": "melina", "cosas": "mesa", "color": "marron"}
    juego.jugada_jugador2 = {"nombre": "maria", "cosas": "madera", "color": "morado"}
    juego.calcular_puntos()

    juego.letra_actual = "A"
    juego.jugada_jugador1 = {"nombre": "Amanda", "cosas": "aro", "color": "amarillo"}
    juego.jugada_jugador2 = {"nombre": "Anibal", "cosas": "andador", "color": "azul"}
    juego.calcular_puntos()

    juego.letra_actual = "D"
    juego.jugada_jugador1 = {"nombre": "Daniela", "cosas": "dedo", "color": "dorado"}
    juego.jugada_jugador2 = {"nombre": "Damian", "cosas": "diamante", "color": "dorado"}
    juego.calcular_puntos()

    assert juego.total_jugador1 == 90
    assert juego.total_jugador2 == 90

    ganador = juego.calcular_ganador()
    assert ganador == "Empate"