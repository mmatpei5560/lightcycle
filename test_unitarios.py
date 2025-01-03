from modelo.vector import Vector
from modelo.cycle import Cycle
from modelo.campojuego import CampoJuego

def msg(clase,metodo,resultado):
    if resultado == True:
        etq_resultado = "Ok"
    else:
        etq_resultado = "Fallo"
    print(f'Clase {clase} - Método {metodo} - {etq_resultado}')

def testSumarVector():
    vector1 = Vector(5,6)
    vector2 = Vector(1,2)
    vector1.sumar(vector2)
    if vector1.x == 6 and vector1.y == 8:
        msg("Vector","sumar",True)
    else:
        msg("Vector","sumar", False)
        

def testClonarVector():
    vector1 = Vector(5,6)
    vector2 = vector1.clonar()

    if vector1 is vector2:
        msg("Vector","clonar",False)
    elif vector1.x == vector2.x and vector1.y == vector2.y:
        msg("Vector","clonar",True)

def testEqVector():
    vector1 = Vector(5,6)
    vector2 = Vector(5,6)
    vector3 = Vector(6,7)

    if vector1 == vector2 and vector1 != vector3:
        msg("Vector","__eq__",True)
    else:
        msg("Vector","__eq__",False)

def testStrVector():
    vector = Vector(5,6)
    if str(vector) == "(5,6)":
        msg("Vector","__str__",True)
    else:
        msg("Vector","__str__",False)

def testChocaCycle():
    cycle1 = Cycle(Vector(9,15),Vector(0,0),"cycle1",(0,0,0))
    cycle2 = Cycle(Vector(15,9),Vector(0,0),"Cycle2",(0,0,0))
    cycle3 = Cycle(Vector(9,30),Vector(0,0),"Cycle3",(0,0,0))
    for i in range(10,16):
        cycle1.camino.append(Vector(i,15))
        cycle2.camino.append(Vector(15,i))
        cycle3.camino.append(Vector(i,30))
        

    if cycle1.choca(cycle2) and not cycle1.choca(cycle3):
        msg("Cycle","choca",True)
    else:
        msg("Cycle","choca",False)

def testChocaConsigoCycle():
    cycle1 = Cycle(Vector(10,10),Vector(0,0),"Cycle1",(0,0,0))
    
    for i in range(11,15):
        cycle1.camino.append(Vector(i,10))
    cycle1.camino.append(Vector(13,10))

    if cycle1.choca_consigo_mismo():
        msg("Cycle","choca_consigo_mismo",True)
    else:
        msg("Cycle","choca_consigo_mismo",False)

def testGetRegionCampoJuego():
    campoJuego = CampoJuego(600,600,50,50)
    test1 = campoJuego.ancho_region == 12
    test2 = campoJuego.alto_region == 12

    region = campoJuego.get_region(Vector(10,10))
    test3 = region[0] == 120 and region[1] == 120 and region[2] == 12 and region[3] == 12
    if test1 and test2 and test3:
        msg("CampoJuego","get_region",True)
    else:
        msg("CampoJuego","get_region",False)


testSumarVector()
testClonarVector()
testEqVector()
testStrVector()
testChocaCycle()
testChocaConsigoCycle()
testGetRegionCampoJuego()