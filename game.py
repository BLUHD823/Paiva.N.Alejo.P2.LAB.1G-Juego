import pygame, sys 
from pygame.locals import *
import sys
from assets import *
from levels import *
from imagenes import *

class Level_1:
    def __init__(self):
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.FPS = 60
        self.CENTER = (self.WIDTH // 2,self.HEIGHT // 2)
        pygame.init()

        self.display = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption("TOUHOU")

        self.fondo = pygame.image.load('.\src\\atardecer}.png')
        self.player = Paleta((self.WIDTH- 1000,self.HEIGHT-100),5,diccionario,diccionario_girado,0.8,-16)
        
        #plataformas
        self.tile_set = Piso((0,self.HEIGHT))
        self.obstaculo_1 = Obstaculo((self.WIDTH // 2, self.HEIGHT- 142),'.\src\obstacul0.png')
        self.obstaculo_2 = Obstaculo((self.WIDTH - 823, self.HEIGHT- 202),'.\src\obstacul0.png')
        self.plataforma = Obstaculo((self.WIDTH -1200, self.HEIGHT- 249),'.\src\plataforma god.png')
        
        self.enemy = Enemy(diccionario_enemigo_girado,diccionario_enemigo,self.plataforma.rect.midtop,2,self.plataforma.rect.topright,self.plataforma.rect.topleft)

        self.group_sprite = pygame.sprite.Group()
        self.group_sprite.add(self.tile_set,self.obstaculo_1,self.obstaculo_2,self.plataforma)

        self.enemies_sprites = pygame.sprite.Group()
        self.enemies_sprites.add(self.enemy)

        self.is_playing = True
        self.pressed = False #BANDERA SALTO
        
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
        
        self.obstaculo_1.draw(self.display)
        self.obstaculo_2.draw(self.display)
        self.plataforma.draw(self.display)
        self.player.update(self.display)
        for enemi in self.enemies_sprites: 
            enemi.update(self.display)
        #colisiones
        colision_v(self.player,self.group_sprite)
        colision_h(self.player,self.group_sprite)
        colision_enemy(self.player,self.enemies_sprites)
        
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: #left
            self.player.mover_x_izq()
        elif keys_pressed[pygame.K_d]: #right
                self.player.mover_x_derecha(self.WIDTH)
        else:
            self.player.status = 'idle'
            self.player.direction.x = 0
        if keys_pressed[pygame.K_SPACE]: #salto
            if self.pressed == False:
                self.player.salto()
                self.pressed = True
            if self.player.direction.y == 0:
                self.pressed = False
        
    def render(self):
        if self.player.life <= 0:
            self.is_playing = False
        pygame.display.flip()
