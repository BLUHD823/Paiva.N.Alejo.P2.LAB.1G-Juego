# import pygame, sys 
# from pygame.locals import *
# import sys
# from assets import *
# from levels import *
# from imagenes import *


# WIDTH = 1280
# HEIGHT = 720
# FPS = 60

# CENTER = (WIDTH // 2,HEIGHT // 2)

# pygame.init()

# display = pygame.display.set_mode((WIDTH,HEIGHT))
# pygame.display.set_caption("TOUHOU")

# player = Paleta((WIDTH- 1000,HEIGHT-200),5,diccionario,diccionario_girado,8,-30)

# tile_set = Piso((0,HEIGHT))

# obstaculo = Obstaculo((WIDTH // 2, HEIGHT- 182))

# fondo = pygame.image.load('C:\\Users\\Alejo\\Desktop\\pygame\\src\\atardecer}.png')

# while True:
#     reloj = pygame.time.Clock()
#     reloj.tick(FPS)

#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT: #QUIT SERÍA LA X DE CERRAR
#             pygame.quit()
#             sys.exit()
    
#     display.blit(fondo,(0,0))
#     display.blit(tile_set.surface, tile_set.rect)
#     display.blit(obstaculo.surface, obstaculo.rect)
#     player.update(display,tile_set) 
#     colision_v(player,obstaculo)
    
#     keys_pressed = pygame.key.get_pressed()
#     if keys_pressed[pygame.K_a]: #left
#         player.mover_x_izq()
#     elif keys_pressed[pygame.K_d]: #right
#         player.mover_x_derecha(WIDTH)
#     else:
#         player.status = 'idle'
#     if keys_pressed[pygame.K_SPACE]: #salto
#         player.salto()
    


#     # pygame.draw.rect(display,(255,255,255),player.rectangulo,2)
#     # pygame.draw.rect(display,(255,255,255),obstaculo.rect,2)
#     pygame.display.flip()