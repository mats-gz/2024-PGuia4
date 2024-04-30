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

def mostrar_menu():
    while True:
        menu_inicial()
        opcion = input("Seleccione el número opción deseado:")

        if opcion == "1":
            jugador1 = jugFutbol("", 0, "", "", "", 0, 0, 0, 0, 0, 0, 0, {})
            jugador1.crear_jugador()

        elif opcion == "2":
            jugador2.actualizar_info()

        elif opcion == "3":
            jugador2.goles_partido()

        elif opcion == "4":
            jugador2.es_goleador()

        elif opcion == "5":
            jugador2.agregar_premios()

        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")


def menu_inicial():
    print("Bienvenido, elige una de las opciones:")
    print("1 - Crear jugador")
    print("2 - Actualizar info")
    print("3 - Promedio de goles")
    print("4 - Tu jugador, ¿Es goleador?")
    print("5 - Agregar premios")
    print("6 - Salir")


# crear jg2 para demostracion beta del menu
jugador2 = jugFutbol("Martina", 17, "defensa", "Independiente", "Argentina", 7, 0, 1, 1, 4, 12, ["Premio1", "Copa Libertadores", "Copa ETE SECH", "Oi Oi Oi"])

mostrar_menu()

