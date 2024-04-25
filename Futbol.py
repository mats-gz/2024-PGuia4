class jugFutbol:
    def __init__(self, nombre, edad, posicion, equipo, pais, numCamisa, goles, partidos, asistencias, tarRoja, tarAmarilla, cantReconocimientos = 0, cantPremios = 0, premios = None):
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
        self.cantReconocimientos = cantReconocimientos
        self.cantPremios = cantPremios
        self.premios = premios if premios is not None else {}

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
        self.cantReconocimientos = int(input("Ingrese cantidad de reconocimientos del jugador:"))

        self.cantPremios = int(input("Ingrese cantidad de premios del jugador:"))
        self.premios = {}  
        for _ in range(self.cantPremios):
            equipo = input("Ingrese el equipo al que le ganó el premio: ")
            premio = input(f"Ingrese el premio que ganó al equipo {equipo}: ")
            self.premios[equipo] = premio

        print(f"Los datos de tu jugador son: {self.nombre} de {self.edad} años, juega de {self.posicion} en {self.equipo}, y en {self.pais}, usa el {self.numCamisa}. Marcó {self.goles} goles y {self.asistencias} asistencias en {self.partidos} partidos, le sacaron {self.tarAmarilla} amarillas y {self.tarRoja} rojas. Ganó estos premios: {self.premios}")


    def actualizar_info(self):
        self.partidos += 1
        self.goles += int(input("¿Cuántos goles hizo?"))
        self.asistencias += int(input("¿Cuántos asistencias hizo?"))
        self.tarRoja += int(input("¿Cuántas tarjetas rojas tuvo?"))
        self.tarAmarilla += int(input("¿Cuántas tarjetas amarillas tuvo?"))
        print(f'Datos actualizados: Cantidad de goles actual: {self.goles}, Cantidad de asistencias: {self.asistencias}, Cantidad de amarillas: {self.tarAmarilla}, Cantidad de rojas: {self.tarRoja}, Jugo un total de {self.partidos} partidos.')

    
    def goles_partido(self):
        promedio = self.goles / self.partidos
        print(f'El promedio de gol por partido de {self.nombre} es = {promedio}')

    
    def es_goleador(self):
        pos = self.posicion.lower()
        if pos == "goleador":
            print("La posición del jugador ingresado es goleador.")
        else:
            print(f"La posición del jugador no es goleador, es {self.posicion}")


    def agregar_premios(self):
        ganoPremios = input("Ganó algun premio? Ingrese si/no:")
        if ganoPremios == "si":
            premiosCant = int(input("¿Cuántos premios ganó?"))
            self.cantPremios += premiosCant
            if premiosCant > 0:
                for _ in range(premiosCant):
                    equipo = input("Ingrese el equipo al que le ganó el premio: ")
                    premio = input(f"Ingrese el premio que ganó al equipo {equipo}: ")
                    self.premios[equipo] = premio
            print(f'Sus premios ahora son: {self.premios}')
        else:
            print("No ganó ningún premio.")


       


# crear jg1 con info vacia
jugador1 = jugFutbol("", 0, "", "", "", 0, 0, 0, 0, 0, 0, 0, {})

# modificar la info vacia llamando la func de crear jugador y almacenando todo en el jugador recien
#jugador1.crear_jugador()

# Crear jugador2 con información proporcionada
jugador2 = jugFutbol("Martina", 17, "Goleador", "independiente", "belgica", 7, 10, 4, 1, 34, 3, 3,premios = {"Barcelona": "Mejor Jugador del Mes", "Real Madrid": "Máximo Goleador de la Temporada", "PSG": "Premio Fair Play"})

# Imprimir los datos del jugador2 con los premios
print(f"Los datos de tu jugador son: {jugador2.nombre} de {jugador2.edad} años, juega de {jugador2.posicion} en {jugador2.equipo}, y en {jugador2.pais}, usa el {jugador2.numCamisa}. Marcó {jugador2.goles} goles y {jugador2.asistencias} asistencias en {jugador2.partidos} partidos, le sacaron {jugador2.tarAmarilla} amarillas y {jugador2.tarRoja} rojas. Gano estos premios {jugador2.premios}")

#jugador2.actualizar_info()
jugador2.goles_partido()
jugador2.agregar_premios()
jugador2.es_goleador()
