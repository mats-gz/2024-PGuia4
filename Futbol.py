class jugFutbol:
    def __init__(self, nombre, edad, posicion, equipo, pais, numCamisa, goles, partidos, asistencias, tarRoja, tarAmarilla, cantPremios = 0, cantReconocimientos = 0, premios = {}):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo
        self.pais = pais
        self.numCamisa = numCamisa
        self.goles = goles
        self.partidos = partidos
        self.asistencias = asistencias
        self.tarRoja = tarRoja
        self.tarAmarilla = tarAmarilla
        self.cantPremios = cantPremios
        self.cantReconocimientos = cantReconocimientos
        self.premios = premios

    def crear_jugador(self):
        self.nombre = input("Ingrese nombre del jugador:")
        self.edad = int(input("Ingrese edad del jugador:"))
        self.posicion = input("Ingrese posicion del jugador:")
        self.equipo = input("Ingrese equipo del jugador:")
        self.pais = input("Ingrese pais del jugador:")
        self.numCamisa = int(input("Ingrese numero de camisa del jugador:"))
        self.goles = int(input("Ingrese goles del jugador:"))
        self.partidos = int(input("Ingrese cantidad de partidos del jugador:"))
        self.asistencias = int(input("Ingrese asistencias del jugador:"))
        self.tarRoja = int(input("Ingrese cantidad de tarjetas rojas del jugador:"))
        self.tarAmarilla = int(input("Ingrese cantidad de tarjetas amarillas del jugador:"))
        self.cantPremios = int(input("Ingrese cantidad de premios del jugador:"))
        self.cantReconocimientos = int(input("Ingrese cantidad de reconocimientos del jugador:"))

        self.premios = {}  
        for _ in range(self.cantPremios):
            equipo = input("Ingrese el equipo al que le ganó el premio: ")
            premio = input(f"Ingrese el premio que ganó al equipo {equipo}: ")
            self.premios[equipo] = premio

        print(f"Los datos de tu jugador son: {self.nombre} de {self.edad} años, juega de {self.posicion} en {self.equipo}, y en {self.pais}, usa el {self.numCamisa}. Marcó {self.goles} goles y {self.asistencias} asistencias en {self.partidos} partidos, le sacaron {self.tarAmarilla} amarillas y {self.tarRoja} rojas. Ganó estos premios: {self.premios}")


# Crear jugador1 con información vacía
jugador1 = jugFutbol("", 0, "", "", "", 0, 0, 0, 0, 0, 0, 0, {})

# Llamar al método crear_jugador para crear un jugador y almacenarlo en jugador1
jugador1.crear_jugador()

# Crear jugador2 con información proporcionada
jugador2 = jugFutbol("Martina", 17, "defensa", "independiente", "belgica", 7, 0, 1, 1, 4, 12 , {"Boca Juniors": "Copa Libertadores", "Real Madrid": "Champions League"})
print(f"Los datos de tu jugador son: {jugador2.nombre} de {jugador2.edad} años, juega de {jugador2.posicion} en {jugador2.equipo}, y en {jugador2.pais}, usa el {jugador2.numCamisa}. Marcó {jugador2.goles} goles y {jugador2.asistencias} asistencias en {jugador2.partidos} partidos, le sacaron {jugador2.tarAmarilla} amarillas y {jugador2.tarRoja} rojas. Ganó estos premios: {jugador2.premios}")
