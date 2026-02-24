import random
class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        #permite mayusculas y minusculas
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()
        #opciones validas
        opciones_validas = {"piedra", "papel", "tijera"}
        if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
            return "invalid"
        
        if jugador1 == jugador2:
            return "empate"
        if (
            (jugador1 == "piedra" and jugador2 == "tijera") or
            (jugador1 == "tijera" and jugador2 == "papel") or
            (jugador1 == "papel" and jugador2 == "piedra")
        ):
            return "jugador1"
        else:
            return "jugador2"

    pass
    
    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"
    pass
    
    def ta_te_ti_ganador(self, tablero):
        # Revisar filas
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] != " ":
                return fila[0]

        # Revisar columnas
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] != " ":
                return tablero[0][col]

        # Revisar diagonales
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
            return tablero[0][2]

        # Verificar si continúa o empate
        for fila in tablero:
            if " " in fila:
                return "continua"
        return "empate"
    pass
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        combinacion = []
        for _ in range(longitud):
            combinacion.append(random.choice(colores_disponibles))
        return combinacion
    pass
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        #limites del tablero
        if not (0 <= desde_fila <= 7 and 0 <= desde_col <= 7 and 0 <= hasta_fila <= 7 and 0 <= hasta_col <= 7):
            return False
        
        # Si no hay movimiento
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        # Debe moverse en línea recta
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        # Movimiento horizontal
        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False

        # Movimiento vertical
        if desde_col == hasta_col:
            paso = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False

        return True
    pass