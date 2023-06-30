import pygame, sys 
from pygame.locals import *
import sys
from assets import *
from levels import *
from imagenes import *

class Level_2:
    def __init__(self):
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.FPS = 60
        self.CENTER = (self.WIDTH // 2,self.HEIGHT // 2)
        self.LIFE = 3
        
        pygame.init()
        #Texto
        self.contador = 0
        self.Font_size = 10
        self.font = pygame.font.SysFont("Pixeled Regular",self.Font_size)
        #Window
        self.display = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption("Level 2")
        #Esenciales
        self.fondo = pygame.image.load('.\src\\DEATH BG.png')
        self.player = Paleta((200,self.HEIGHT-100),5,diccionario,diccionario_girado,0.8,-16,self.LIFE)
        self.game_over_bg = pygame.image.load('.\src\\game over.png')
        self.win_bg = pygame.image.load('src\\good end.png')
        #botones
        self.paused = Options((self.WIDTH // 2, 323),pausa['GAME_PAUSED'])
        self.resume = Options((self.WIDTH // 2, 403),pausa['RESUME'])
        self.quit = Options((self.WIDTH // 2, 463),pausa['QUIT'])
        #UI
        self.heart_1 = Life((35,735),'.\src\\heart.png')
        self.heart_2 = Life((80,735),'.\src\\heart.png')
        self.heart_3 = Life((125,735),'.\src\\heart.png')
        self.coin_1 = Coins((35,35),coin,bigger_coin,False)
        self.counter = Texto(self.font,(255,255,255),45,12)
        #Volumen
        self.volumen_up = sonido['WHITE_UP'][0]
        self.volumen_down = sonido['WHITE_DOWN'][0]
        self.volumen_mute = sonido['WHITE_MUTE'][0]
        #plataformas
        self.piso =  Obstaculo((145, 720),'.\src\\future piso.png')   #future piso
        self.obstaculo_1 = Obstaculo((1200, 410),'.\src\\future piso 3.5.png')
        self.obstaculo_2 = Obstaculo((800, 620),'.\src\\future piso 3.png')
        self.obstaculo_3 = Obstaculo((1000, 285),'.\src\\future piso 3.75.png')
        #plataforma enemigos
        self.plataforma_1 = Obstaculo((500, 670),'.\src\\future piso 2.png')
        self.plataforma_2 = Obstaculo((1100, 540),'.\src\\future piso 4.png')
        self.plataforma_3 = Obstaculo((410, 280),'.\src\\future piso 5.png')
        self.obstaculo_4 = Obstaculo((780, 220),'.\src\\future piso 3.5.png')
        #monedas
        self.coin_colleccionable_1 = Coins((self.obstaculo_3.rect.x + 20,self.obstaculo_3.rect.y - 10),coin,bigger_coin,True)
        self.coin_colleccionable_2 = Coins((800,self.obstaculo_2.rect.y - 10),coin,bigger_coin,True)
        self.coin_colleccionable_3 = Coins((self.plataforma_1.rect.x + 160,self.plataforma_1.rect.y - 10),coin,bigger_coin,True)
        self.coin_colleccionable_4 = Coins((self.plataforma_2.rect.x + 60,self.plataforma_2.rect.y - 10),coin,bigger_coin,True)
        self.coin_colleccionable_4 = Coins((self.obstaculo_4.rect.x + 47,self.obstaculo_4.rect.y - 10),coin,bigger_coin,True)
        self.coin_colleccionable_5 = Coins((640,226),coin,bigger_coin,True)
        self.coin_colleccionable_6 = Coins((self.plataforma_3.rect.x + 106,self.plataforma_3.rect.y - 10),coin,bigger_coin,True)
        #enemigos
        self.enemy = Enemy(diccionario_cyrax_girado,diccionario_cyrax,self.plataforma_1.rect,2,'right')
        self.enemy_2 = Enemy(diccionario_cyrax_girado,diccionario_cyrax,self.plataforma_2.rect,2,'left')
        self.enemy_3 = Enemy(diccionario_cyrax_girado,diccionario_cyrax,self.plataforma_3.rect,1,'right')
        self.enemy_4 = Enemy(diccionario_cyrax_girado,diccionario_cyrax,self.obstaculo_4.rect,1,'right')
        self.enemy_5 = Enemy(diccionario_cyrax_girado,diccionario_cyrax,self.plataforma_3.rect,1,'left')
        #grupos plataformas
        self.group_sprite = pygame.sprite.Group()
        self.group_sprite.add(self.piso,self.obstaculo_1,self.obstaculo_2,self.plataforma_1,self.obstaculo_3,self.plataforma_2,self.plataforma_3,self.obstaculo_4)
        #grupo enemigos
        self.enemies_sprites = pygame.sprite.Group()
        self.enemies_sprites.add(self.enemy,self.enemy_2,self.enemy_3,self.enemy_4,self.enemy_5)
        #grupo vida
        self.current_health = pygame.sprite.Group()
        self.current_health.add(self.heart_1,self.heart_2,self.heart_3)
        #grupo monedas
        self.collectible_coins = pygame.sprite.Group()
        self.collectible_coins.add(self.coin_colleccionable_1,self.coin_colleccionable_2,self.coin_colleccionable_3,self.coin_colleccionable_4,self.coin_colleccionable_5,
                                   self.coin_colleccionable_6)
        #estado del nivel
        self.is_playing = True
        self.pressed = False #BANDERA SALTO
        self.game_over = False
        self.complete_collection = False
        #replay estado
        self.replay = False
        
    def play(self):
        self.pause = False
        while self.is_playing:
            reloj = pygame.time.Clock()
            reloj.tick(self.FPS)
            self.handler_events()
            if self.game_over == False and self.pause == False and self.complete_collection == False:
                self.update()
                self.render()
            elif self.pause == True:
                self.paused.draw(self.display)
                self.resume.draw(self.display)
                self.quit.draw(self.display)
                if self.quit.clicked:
                    self.is_playing = False
                    self.quit.clicked = False
                    self.replay = True
                if self.resume.clicked:
                    self.pause = False
                    self.resume.clicked = False
                print(self.is_playing)
                self.render()
            elif self.game_over:
                self.display.blit(self.game_over_bg,(0,0))
                self.render()
            if self.complete_collection:
                self.display.blit(self.win_bg,(0,0))
                self.render()

    def handler_events(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: #QUIT SERÍA LA X DE CERRAR
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN: # Evento de presionar una tecla
                if evento.key == pygame.K_ESCAPE and self.pause == False: # Pausa Menu
                    pygame.mixer.music.pause()#pausa la música
                    self.pause = True
                elif evento.key == pygame.K_ESCAPE and self.pause == True:# Despausa
                    pygame.mixer.music.unpause()#despausa la música
                    self.pause = False
                elif evento.key == pygame.K_SPACE and self.game_over == True:# Game Over
                    self.is_playing = False
                    self.replay = True
                elif evento.key == pygame.K_SPACE and self.complete_collection == True:# Win
                    self.is_playing = False
                    self.replay = True    
    def update(self):
        self.display.blit(self.fondo,(0,0))
        #terrenos
        for terrain in self.group_sprite:
            terrain.draw(self.display)
        #enemigos
        self.player.update(self.display)
        for enemi in self.enemies_sprites: 
            enemi.update(self.display)
        #vida actual
        for corazon in self.current_health:
            corazon.draw(self.display)
        self.coin_1.draw(self.display)
        for moneda in self.collectible_coins:
            moneda.draw(self.display)
        #Texto
        self.counter.draw_text(self.display)
        #colisiones
        colision_v(self.player,self.group_sprite)
        colision_h(self.player,self.group_sprite)
        colision_enemy(self.player,self.enemies_sprites,self.current_health)
        collect_coins(self.player,self.collectible_coins,self.counter)
        #Monedas totales coleccionadas:
        if len(self.collectible_coins) == 0:
            self.complete_collection = True
        #Cae fuera del mapa
        if self.player.rect.bottom >= self.HEIGHT:
            self.player.life = 0
        #Teclas
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
        if self.player.life == 0:
            self.game_over = True
        if keys_pressed[pygame.K_UP] and pygame.mixer.music.get_volume() < 1.0: #Fecha para arriba
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)#Sube volumen
            self.display.blit(self.volumen_up,(1100,50))
        elif keys_pressed[pygame.K_DOWN] and pygame.mixer.music.get_volume() > 0.0: #Fecha para abajo
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)#Baja volumen
            self.display.blit(self.volumen_down,(1100,50))
        elif keys_pressed[pygame.K_m]:#Mutear con tecla m
            pygame.mixer.music.set_volume(0.0)
        if  pygame.mixer.music.get_volume() == 0.0: #En caso 0.0
            self.display.blit(self.volumen_mute,(1100,50))#Mostrar icono de mute
            
    def render(self):
        pygame.display.flip()
    def reset(self):
        #estados reset
        self.is_playing = True
        self.pressed = False #BANDERA SALTO
        self.game_over = False
        #jugador y enemigos reset
        self.player = Paleta((200,self.HEIGHT-100),5,diccionario,diccionario_girado,0.8,-16,self.LIFE)
        self.enemy = Enemy(diccionario_cyrax_girado,diccionario_cyrax,self.plataforma_1.rect,2,'right')
        self.enemy_2 = Enemy(diccionario_cyrax_girado,diccionario_cyrax,self.plataforma_2.rect,2,'left')
        self.enemy_3 = Enemy(diccionario_cyrax_girado,diccionario_cyrax,self.plataforma_3.rect,1,'right')
        self.enemy_4 = Enemy(diccionario_cyrax_girado,diccionario_cyrax,self.obstaculo_4.rect,1,'right')
        self.enemy_5 = Enemy(diccionario_cyrax_girado,diccionario_cyrax,self.plataforma_3.rect,1,'left')
        self.counter = Texto(self.font,(255,255,255),45,12) #draw_text(self.Text,self.font,(255,255,255),45,12,self.display)
        #grupos reset
        self.group_sprite.empty()
        self.group_sprite.add(self.piso,self.obstaculo_1,self.obstaculo_2,self.plataforma_1,self.obstaculo_3,self.plataforma_2,self.plataforma_3,self.obstaculo_4)
        self.enemies_sprites.empty()
        self.enemies_sprites.add(self.enemy,self.enemy_2,self.enemy_3,self.enemy_4,self.enemy_5)
        self.current_health.empty()
        self.current_health.add(self.heart_1,self.heart_2,self.heart_3)
        self.collectible_coins.empty()
        self.collectible_coins.add(self.coin_colleccionable_1,self.coin_colleccionable_2,self.coin_colleccionable_3,self.coin_colleccionable_4,self.coin_colleccionable_5,self.coin_colleccionable_6)