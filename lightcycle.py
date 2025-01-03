import pygame
from modelo.cycle import Cycle
from modelo.vector import Vector
from modelo.campojuego import CampoJuego
from logica_negocio.reglas import Reglas
     
# Inicializar pygame
pygame.init()
ventana = pygame.display.set_mode((600,600))
pygame.display.set_caption("Lightcycle")

# Inicializar variables
campo_juego = CampoJuego(600,600,50,50)
cycle1 = Cycle(Vector(40,40),Vector(0,-1),"Jugador 2",(255,0,0))
cycle2 = Cycle(Vector(10,40),Vector(0,-1),"Jugador 1",(0,0,255))
velocidad = 3 #fps
reglas_juego = Reglas(campo_juego.columnas,campo_juego.filas)
jugando = True
usuario_cierra_ventana = False
ganador = None



# Dibujar lineas del campo de juego
lineas_campo_juego = campo_juego.get_lista_lineas()
for coor_linea in lineas_campo_juego:
    pygame.draw.line(ventana,(0,100,0),coor_linea[0],coor_linea[1])


# Bucle del juego
while jugando and not usuario_cierra_ventana:

    teclas_pulsadas = [] # lista de teclas pulsadas por el usuario en esta iteración
    
    # Control de eventos
    #   - Cierre al pulsar el botón x
    #   - Pulsaciones de teclas de movimiento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            usuario_cierra_ventana = True
        if event.type == pygame.KEYDOWN:
            if event.key in Reglas.TECLAS_MOVIMIENTO:
                teclas_pulsadas.append(event.key)
    
    # A partir de la lista de teclas pulsadas, se decide el siguiente 
    # sentido de movimiento de los "cycle"
    for tecla in teclas_pulsadas:
        reglas_juego.gestionar_movimiento(tecla,cycle1,cycle2)

    # Los "cycle" se mueven según su sentido de movimiento
    reglas_juego.avanzar(cycle1,cycle2)

    # Se comprueba si hay un ganador de acuerdo con las reglas del juego
    ganador = reglas_juego.comprobar_ganador(cycle1,cycle2)
    
    # Si hay un ganador, se escribe su nombre en pantalla y se detiene el juego
    if ganador != None:
        fuente = pygame.font.Font(None,50)
        texto_superficie = fuente.render(f'Gana: {ganador.nombre}', True, ganador.color)
        texto_rect = texto_superficie.get_rect(center=(300,300))
        ventana.blit(texto_superficie, texto_rect)
        jugando = False

    # Se representan los "cycle" en pantalla
    pygame.draw.rect(ventana,cycle1.color,campo_juego.get_region(cycle1.get_posicion_actual()))
    pygame.draw.rect(ventana,cycle2.color,campo_juego.get_region(cycle2.get_posicion_actual()))

    # Refresco de pantalla y control de fps
    pygame.display.flip()
    pygame.time.Clock().tick(velocidad)

# Una vez terminado el juego (porque hubo un ganador) se espera hasta
# que el usuario pulse el botón 'x'
while not usuario_cierra_ventana:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            usuario_cierra_ventana = True