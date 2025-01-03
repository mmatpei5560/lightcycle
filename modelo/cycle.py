from modelo.vector import Vector

class Cycle:

    def __init__(self, pos_inicial: Vector, sentido: Vector, nombre:str, color):
        self.sentido = sentido
        self.camino =  [pos_inicial]
        self.nombre = nombre
        self.color = color

    def avanzar(self):
        long_camino = len(self.camino)
        cabeza_actual = self.camino[-1]
        nueva_cabeza = cabeza_actual.clonar()

        nueva_cabeza.sumar(self.sentido)
        self.camino.append(nueva_cabeza)

    def set_sentido(self, sentido:Vector):
        self.sentido = sentido

    def get_camino(self):
        return self.camino
    
    def get_posicion_actual(self):
        return self.camino[-1]
    
    def choca(self, otro_cycle:"Cycle"):
         return None
    
    def choca_consigo_mismo(self):
         return None
