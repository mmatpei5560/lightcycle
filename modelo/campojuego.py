from modelo.vector import Vector

class CampoJuego:

    def __init__(self, ancho:float, alto:float, columnas:float, filas:float):
        self.ancho = ancho
        self.alto = alto
        self.columnas = columnas
        self.filas = filas
        self.ancho_region = ancho/columnas
        self.alto_region = alto/filas
    
    def get_region(self,vector_posicion:Vector):
        return None

    def get_lista_lineas(self):
        lista_lineas = []
        for col in range(self.columnas):
            lista_lineas.append([(col*self.ancho_region,0),(col*self.ancho_region,self.alto)])
        for fila in range(self.filas):
            lista_lineas.append([(0,fila*self.alto_region),(self.ancho,fila*self.alto_region)])
        return lista_lineas
