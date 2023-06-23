import pygame

diccionario = {
    'idle_animation' : [pygame.image.load("./idle/quieto chico 2.png"),
                pygame.image.load("./idle/quieto chico 3.png"),
                pygame.image.load("./idle/quieto chico 4.png"),
                pygame.image.load("./idle/quieto chico.png")],
    
    'walking_animation' :[pygame.image.load("./running/walking_1.png"),
                  pygame.image.load("./running/walking_2.png"),
                  pygame.image.load("./running/walking_3.png"),
                  pygame.image.load("./running/walking_4.png")],
    
    'jumping_animation' : [
          pygame.image.load("./jumping/salto.png"),
          ]
}

diccionario_girado = {
    'idle_animation' : [pygame.image.load("./idle/quieto chico 2.png"),
                pygame.image.load("./idle/quieto chico 3.png"),
                pygame.image.load("./idle/quieto chico 4.png"),
                pygame.image.load("./idle/quieto chico.png")],
    
    'walking_animation' :[pygame.image.load("./running/walking_1.png"),
                  pygame.image.load("./running/walking_2.png"),
                  pygame.image.load("./running/walking_3.png"),
                  pygame.image.load("./running/walking_4.png")],
    
    'jumping_animation' : [
          pygame.image.load("./jumping/salto.png"),
          ]
}




def girar_imagenes(diccionario,flip_x,flip_y):
    
    for lista in diccionario.values():
        for imagen in range(len(lista)):
            lista[imagen] = pygame.transform.flip(lista[imagen],flip_x,flip_y)


def reescalar_imagenes(diccionario):
    for lista in diccionario.values():
        for i in range(len(lista)):
            lista[i] = pygame.transform.scale(lista[i],(80,103))

reescalar_imagenes(diccionario)
reescalar_imagenes(diccionario_girado)

girar_imagenes(diccionario_girado,True,False)

# personaje_izquierda = girar_imagenes(idle_animation,True,False)