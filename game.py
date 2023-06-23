import pygame, sys 
from pygame.locals import *
import sys
from assets import *
from levels import *
from imagenes import *

class Game:
    def __init__(self):
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.FPS = 60
        self.CENTER = (self.WIDTH // 2,self.HEIGHT // 2)
        pygame.init()
        self.display = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption("TOUHOU")
        self.player = Paleta((self.WIDTH- 1000,self.HEIGHT-200),5,diccionario,diccionario_girado,10,-20)
        self.tile_set = Piso((0,self.HEIGHT))
        self.obstaculo = Obstaculo((self.WIDTH // 2, self.HEIGHT- 182))
        self.fondo = pygame.image.load('.\src\\atardecer}.png')
        self.is_playing = False
        
    def play(self):
        self.is_playing = True

        while self.is_playing:
            reloj = pygame.time.Clock()
            reloj.tick(self.FPS)
            
            self.handler_events()
            self.update()
            self.render()

    def handler_events(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: #QUIT SERÍA LA X DE CERRAR
                pygame.quit()
                sys.exit()

        
    def update(self):
        self.display.blit(self.fondo,(0,0))
        self.display.blit(self.tile_set.surface, self.tile_set.rect)
        self.display.blit(self.obstaculo.surface, self.obstaculo.rect)
        self.player.update(self.display,self.tile_set) 
        colision_v(self.player,self.obstaculo)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: #left
            self.player.mover_x_izq()
        elif keys_pressed[pygame.K_d]: #right
                self.player.mover_x_derecha(self.WIDTH)
        else:
            self.player.status = 'idle'
        if keys_pressed[pygame.K_SPACE]: #salto
            
            self.player.salto()
        
        print(self.player.rectangulo.y)

        
    def render(self):
        pygame.display.flip()
