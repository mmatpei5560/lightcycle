from modelo.vector import Vector
from modelo.cycle import Cycle
import pygame

class Reglas:

    TECLAS_MOVIMIENTO = [pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a]

    def __init__(self,columnas, filas):
        self.columnas = columnas
        self.filas = filas

    def gestionar_movimiento(self,tecla,cycle1:Cycle,cycle2:Cycle):
        sentido = self.get_sentido(tecla)
        if tecla in [pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT]:
            cycle1.set_sentido(sentido)
        if tecla in [pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a]:
            cycle2.set_sentido(sentido)

    def get_sentido(self, tecla):
        if tecla == pygame.K_UP or tecla == pygame.K_w:
            return Vector(0,-1)
        if tecla == pygame.K_RIGHT or tecla == pygame.K_d:
            return Vector(1,0)
        if tecla == pygame.K_DOWN or tecla == pygame.K_s:
            return Vector(0,1)
        if tecla == pygame.K_LEFT or tecla == pygame.K_a:
            return Vector(-1,0)
        
    def avanzar(self,cycle1:Cycle,cycle2:Cycle):
        cycle1.avanzar()
        cycle2.avanzar()

    def comprobar_ganador(self, cycle1, cycle2):
        if self.fuera_pista(cycle1):
            return cycle2
        elif self.fuera_pista(cycle2):
            return cycle1
        elif cycle1.choca(cycle2):
            return cycle2
        elif cycle2.choca(cycle1):
            return cycle1
        elif cycle1.choca_consigo_mismo():
            return cycle2
        elif cycle2.choca_consigo_mismo():
            return cycle1
        return None
    
    def fuera_pista(self,cycle:Cycle):
        posicion_actual = cycle.get_posicion_actual()
        if posicion_actual.x < 0:
            return True
        elif posicion_actual.x >= self.columnas:
            return True
        elif posicion_actual.y < 0:
            return True
        elif posicion_actual.y >= self.filas:
            return True
        return False
