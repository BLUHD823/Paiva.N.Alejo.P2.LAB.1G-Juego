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
          ],
    'falling_animation' : [
          pygame.image.load("./falling/fall.png"),
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
          ],
    'falling_animation' : [
          pygame.image.load("./falling/fall.png"),
          ]
}

diccionario_enemigo = {
    'idle_animation' : [pygame.image.load("./sub zero/IDLE/0.png"),
                pygame.image.load("./sub zero/IDLE/1.png"),
                pygame.image.load("./sub zero/IDLE/2.png"),
                pygame.image.load("./sub zero/IDLE/3.png"),
                pygame.image.load("./sub zero/IDLE/4.png"),
                pygame.image.load("./sub zero/IDLE/5.png"),
                pygame.image.load("./sub zero/IDLE/6.png")],
    
    'walking_animation' :[pygame.image.load("./sub zero/WALKING/21.png"),
                  pygame.image.load("./sub zero/WALKING/22.png"),
                  pygame.image.load("./sub zero/WALKING/23.png"),
                  pygame.image.load("./sub zero/WALKING/24.png"),
                  pygame.image.load("./sub zero/WALKING/25.png"),
                  pygame.image.load("./sub zero/WALKING/26.png")],
    
    'attack_animation' : [
          pygame.image.load("./sub zero/ATTACK/0.png"),
          pygame.image.load("./sub zero/ATTACK/1.png"),
          pygame.image.load("./sub zero/ATTACK/2.png"),
          pygame.image.load("./sub zero/ATTACK/3.png")],
    'death_animation' : [
          pygame.image.load("./sub zero/DEATH/18.png"),
          pygame.image.load("./sub zero/DEATH/19.png"),
          pygame.image.load("./sub zero/DEATH/20.png")]
}

diccionario_enemigo_girado = {
    'idle_animation' : [pygame.image.load("./sub zero/IDLE/0.png"),
                pygame.image.load("./sub zero/IDLE/1.png"),
                pygame.image.load("./sub zero/IDLE/2.png"),
                pygame.image.load("./sub zero/IDLE/3.png"),
                pygame.image.load("./sub zero/IDLE/4.png"),
                pygame.image.load("./sub zero/IDLE/5.png"),
                pygame.image.load("./sub zero/IDLE/6.png")],
    
    'walking_animation' :[pygame.image.load("./sub zero/WALKING/21.png"),
                  pygame.image.load("./sub zero/WALKING/22.png"),
                  pygame.image.load("./sub zero/WALKING/23.png"),
                  pygame.image.load("./sub zero/WALKING/24.png"),
                  pygame.image.load("./sub zero/WALKING/25.png"),
                  pygame.image.load("./sub zero/WALKING/26.png")],
    
    'attack_animation' : [
          pygame.image.load("./sub zero/ATTACK/0.png"),
          pygame.image.load("./sub zero/ATTACK/1.png"),
          pygame.image.load("./sub zero/ATTACK/2.png"),
          pygame.image.load("./sub zero/ATTACK/3.png")],
    'death_animation' : [
          pygame.image.load("./sub zero/DEATH/18.png"),
          pygame.image.load("./sub zero/DEATH/19.png"),
          pygame.image.load("./sub zero/DEATH/20.png")]
}

coin = {
    'animation' : [pygame.image.load("./golden_coin/0.png"),
                pygame.image.load("./golden_coin/1.png"),
                pygame.image.load("./golden_coin/2.png"),
                pygame.image.load("./golden_coin/3.png")],
}

bigger_coin = {
    'animation' : [pygame.image.load("./golden_coin/0.png"),
                pygame.image.load("./golden_coin/1.png"),
                pygame.image.load("./golden_coin/2.png"),
                pygame.image.load("./golden_coin/3.png")],
}




def girar_imagenes(diccionario,flip_x,flip_y):
    
    for lista in diccionario.values():
        for imagen in range(len(lista)):
            lista[imagen] = pygame.transform.flip(lista[imagen],flip_x,flip_y)


def reescalar_imagenes(diccionario,dimensiones):
    for lista in diccionario.values():
        for i in range(len(lista)):
            lista[i] = pygame.transform.scale(lista[i],dimensiones)

reescalar_imagenes(diccionario,(80,103))
reescalar_imagenes(diccionario_girado,(80,103))
reescalar_imagenes(bigger_coin,(30,30))

girar_imagenes(diccionario_girado,True,False)
girar_imagenes(diccionario_enemigo_girado,True,False)

menu ={
    'BG' : pygame.image.load('.\MENU\\FONDO.png'),
    'GAME_LEVELS' : pygame.image.load('./MENU/GAME LEVELS.png'),
    'OPTIONS' : pygame.image.load('./MENU/OPTIONS.png'),
    'QUIT' : pygame.image.load('./MENU/QUIT.png'),
    'TITULO' : pygame.image.load('./MENU/título level 1.png'),
    'PORTADA_1' : pygame.image.load('./MENU/level_portada.png')
}