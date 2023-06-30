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
    'idle_animation' : [pygame.image.load("./enemies/IDLE/0.png"),
                pygame.image.load("./enemies/IDLE/1.png"),
                pygame.image.load("./enemies/IDLE/2.png"),
                pygame.image.load("./enemies/IDLE/3.png"),
                pygame.image.load("./enemies/IDLE/4.png"),
                pygame.image.load("./enemies/IDLE/5.png"),
                pygame.image.load("./enemies/IDLE/6.png")],
    
    'walking_animation' :[pygame.image.load("./enemies/WALKING/21.png"),
                  pygame.image.load("./enemies/WALKING/22.png"),
                  pygame.image.load("./enemies/WALKING/23.png"),
                  pygame.image.load("./enemies/WALKING/24.png"),
                  pygame.image.load("./enemies/WALKING/25.png"),
                  pygame.image.load("./enemies/WALKING/26.png")],
    
    'attack_animation' : [
          pygame.image.load("./enemies/ATTACK/0.png"),
          pygame.image.load("./enemies/ATTACK/1.png"),
          pygame.image.load("./enemies/ATTACK/2.png"),
          pygame.image.load("./enemies/ATTACK/3.png")],
    'death_animation' : [
          pygame.image.load("./enemies/DEATH/18.png"),
          pygame.image.load("./enemies/DEATH/19.png"),
          pygame.image.load("./enemies/DEATH/20.png")]
}

diccionario_enemigo_girado = {
    'idle_animation' : [pygame.image.load("./enemies/IDLE/0.png"),
                pygame.image.load("./enemies/IDLE/1.png"),
                pygame.image.load("./enemies/IDLE/2.png"),
                pygame.image.load("./enemies/IDLE/3.png"),
                pygame.image.load("./enemies/IDLE/4.png"),
                pygame.image.load("./enemies/IDLE/5.png"),
                pygame.image.load("./enemies/IDLE/6.png")],
    
    'walking_animation' :[pygame.image.load("./enemies/WALKING/21.png"),
                  pygame.image.load("./enemies/WALKING/22.png"),
                  pygame.image.load("./enemies/WALKING/23.png"),
                  pygame.image.load("./enemies/WALKING/24.png"),
                  pygame.image.load("./enemies/WALKING/25.png"),
                  pygame.image.load("./enemies/WALKING/26.png")],
    
    'attack_animation' : [
          pygame.image.load("./enemies/ATTACK/0.png"),
          pygame.image.load("./enemies/ATTACK/1.png"),
          pygame.image.load("./enemies/ATTACK/2.png"),
          pygame.image.load("./enemies/ATTACK/3.png")],
    'death_animation' : [
          pygame.image.load("./enemies/DEATH/18.png"),
          pygame.image.load("./enemies/DEATH/19.png"),
          pygame.image.load("./enemies/DEATH/20.png")]
}

diccionario_cyrax = {
    'walking_animation' :[pygame.image.load("./enemies/CYRAX WALKING/0.png"),
                  pygame.image.load("./enemies/CYRAX WALKING/1.png"),
                  pygame.image.load("./enemies/CYRAX WALKING/2.png"),
                  pygame.image.load("./enemies/CYRAX WALKING/3.png"),
                  pygame.image.load("./enemies/CYRAX WALKING/4.png"),
                  pygame.image.load("./enemies/CYRAX WALKING/5.png"),
                  pygame.image.load("./enemies/CYRAX WALKING/6.png"),
                  pygame.image.load("./enemies/CYRAX WALKING/7.png")],
    
    'attack_animation' : [
          pygame.image.load("./enemies/CYRAX ATTACK/8.png"),
          pygame.image.load("./enemies/CYRAX ATTACK/9.png"),
          pygame.image.load("./enemies/CYRAX ATTACK/10.png")
          ],
    'death_animation' : [
          pygame.image.load("./enemies/CYRAX DEATH/1.png"),
          pygame.image.load("./enemies/CYRAX DEATH/2.png"),
          pygame.image.load("./enemies/CYRAX DEATH/3.png"),
          pygame.image.load("./enemies/CYRAX DEATH/4.png"),
          pygame.image.load("./enemies/CYRAX DEATH/5.png")]
}

diccionario_cyrax_girado = {
    'walking_animation' :[pygame.image.load("./enemies/CYRAX WALKING/0.png"),
                  pygame.image.load("./enemies/CYRAX WALKING/1.png"),
                  pygame.image.load("./enemies/CYRAX WALKING/2.png"),
                  pygame.image.load("./enemies/CYRAX WALKING/3.png"),
                  pygame.image.load("./enemies/CYRAX WALKING/4.png"),
                  pygame.image.load("./enemies/CYRAX WALKING/5.png"),
                  pygame.image.load("./enemies/CYRAX WALKING/6.png"),
                  pygame.image.load("./enemies/CYRAX WALKING/7.png")],
    
    'attack_animation' : [
          pygame.image.load("./enemies/CYRAX ATTACK/8.png"),
          pygame.image.load("./enemies/CYRAX ATTACK/9.png"),
          pygame.image.load("./enemies/CYRAX ATTACK/10.png")
          ],
    'death_animation' : [
          pygame.image.load("./enemies/CYRAX DEATH/1.png"),
          pygame.image.load("./enemies/CYRAX DEATH/2.png"),
          pygame.image.load("./enemies/CYRAX DEATH/3.png"),
          pygame.image.load("./enemies/CYRAX DEATH/4.png"),
          pygame.image.load("./enemies/CYRAX DEATH/5.png")]
}

coin = {
    'animation' : [pygame.image.load("./golden_coin/0.png"),
                pygame.image.load("./golden_coin/1.png"),
                pygame.image.load("./golden_coin/2.png"),
                pygame.image.load("./golden_coin/3.png")],
}

sonido ={
    'BLACK_UP' : [pygame.image.load('.\Volume\\BLACK UP.png')],
    'BLACK_DOWN' : [pygame.image.load('.\Volume\\BLACK DOWN.png')],
    'BLACK_MUTE' : [pygame.image.load('.\Volume\\BLACK MUTE.png')],
    'WHITE_UP' : [pygame.image.load('.\Volume\\WHITE UP.png')],
    'WHITE_DOWN' : [pygame.image.load('.\Volume\\WHITE DOWN.png')],
    'WHITE_MUTE' : [pygame.image.load('.\Volume\\WHITE MUTE.png')]
}

bigger_coin = {
    'animation' : [pygame.image.load("./golden_coin/0.png"),
                pygame.image.load("./golden_coin/1.png"),
                pygame.image.load("./golden_coin/2.png"),
                pygame.image.load("./golden_coin/3.png")],
}

menu ={
    'BG' : pygame.image.load('.\MENU\\FONDO.png'),
    'GAME_LEVELS' : pygame.image.load('./MENU/GAME LEVELS.png'),
    'OPTIONS' : pygame.image.load('./MENU/OPTIONS.png'),
    'QUIT' : pygame.image.load('./MENU/QUIT.png'),
    'TITULO' : pygame.image.load('./MENU/título level 1.png'),
    'PORTADA_1' : pygame.image.load('./MENU/level_portada.png'),
    'PORTADA_2' : pygame.image.load('./MENU/level_portada_2.png'),
    'ARROW' : pygame.image.load('./MENU/pixel arrow.png')
}

pausa ={
    'GAME_PAUSED' : pygame.image.load('.\PAUSED MENU\\GAME PAUSED.png'),
    'RESUME' : pygame.image.load('.\PAUSED MENU\\RESUME.png'),
    'QUIT' : pygame.image.load('.\PAUSED MENU\\QUIT.png')
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
reescalar_imagenes(sonido,(64,50))

girar_imagenes(diccionario_girado,True,False)
girar_imagenes(diccionario_enemigo_girado,True,False)
girar_imagenes(diccionario_cyrax_girado,True,False)

