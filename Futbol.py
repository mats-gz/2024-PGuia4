#metodo inicial y llamar a los metodos restantes

class jugFutbol:
    def __init__(self, nombre, edad, posicion, equipo, pais, numCamisa, goles, partidos, asistencias, tarRoja, tarAmarilla, cantPremios, cantReconocimientos):
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


#primera act y primer modulo, crear el jugador

def crear_jugador():
    nombre = input("Ingrese nombre del jugador:")
    edad = int(input("Ingrese edad del jugador:"))
    posicion = input("Ingrese posicion del jugador:")
    equipo = input("Ingrese equipo del jugador:")
    pais = input("Ingrese pais del jugador:")
    numCamisa = int(input("Ingrese numero de camisa del jugador:"))
    goles = int(input("Ingrese goles del jugador:"))
    partidos = int(input("Ingrese cantidad de partidos del jugador:"))
    asistencias = int(input("Ingrese asistencias del jugador:"))
    tarRoja = int(input("Ingrese cantidad de tarjetas rojas del jugador:"))
    tarAmarilla = int(input("Ingrese cantidad de tarjetas amarillas del jugador:"))
    cantPremios = int(input("Ingrese cantidad de premios del jugador:"))
    cantReconocimientos = int(input("Ingrese cantidad de reconocimientos del jugador:"))

    return jugFutbol(nombre, edad, posicion, equipo, pais, numCamisa, goles, partidos, asistencias, tarRoja, tarAmarilla, cantPremios, cantReconocimientos)


jugador1 = crear_jugador()

print("Nombre:", jugador1.nombre)
print("Edad:", jugador1.edad)
print("Posición:", jugador1.posicion)
print("Equipo:", jugador1.equipo)
print("País:", jugador1.pais)
print("Número de Camisa:", jugador1.numCamisa)
print("Goles:", jugador1.goles)
print("Partidos:", jugador1.partidos)
print("Asistencias:", jugador1.asistencias)
print("Tarjetas Rojas:", jugador1.tarRoja)
print("Tarjetas Amarillas:", jugador1.tarAmarilla)
print("Cantidad de Premios:", jugador1.cantPremios)
print("Cantidad de Reconocimientos:", jugador1.cantReconocimientos)

        
