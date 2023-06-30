import pygame, sys 
from game import Level_1
from game_2 import Level_2
from assets import Options
from imagenes import *

class Game():
    def __init__(self) -> None:
        self.level = Level_1()
        self.level_2 = Level_2()
        # game.play()
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.FPS = 60
        self.sprites = menu
        self.display = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption("MENU")
        #Botones y portadas de niveles
        self.fondo = menu['BG']
        self.game_levels = Options((self.WIDTH // 2, self.HEIGHT - 337),self.sprites['GAME_LEVELS'])
        self.escape = Options((self.WIDTH // 2, self.HEIGHT - 263),self.sprites['QUIT'])
        self.level_1_portada =  Options((self.WIDTH // 2, 450),self.sprites['PORTADA_1'])
        self.level_2_portada =  Options((self.WIDTH // 2, 680),self.sprites['PORTADA_2'])
        self.go_back =  Options((50, 715),self.sprites['ARROW'])
        #Musica
        pygame.mixer.music.load('.\MUSIC\Star wars Episode III soundtrack - Battle over Coruscant.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)#Funciona de 0.0 a 1.0
        pygame.init()
        #Volumen
        self.volumen_up = sonido['WHITE_UP'][0]
        self.volumen_down = sonido['WHITE_DOWN'][0]
        self.volumen_mute = sonido['WHITE_MUTE'][0]
        #Estados
        self.select_option =  True
        self.first_level = False
        self.second_level = False
        self.running = True
    def run(self):
        while self.running:
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
            elif evento.type == pygame.KEYDOWN: # Evento de presionar una tecla
                if evento.key == pygame.K_1 and self.select_option == False:
                    self.first_level = True
                if evento.key == pygame.K_2 and self.select_option == False:
                    self.second_level = True
    def update(self):
            #Fondo
            self.display.blit(self.fondo,(0,0))

            #Tecla pulsada
            keys_pressed = pygame.key.get_pressed()
            #Teclas sonido
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
            
            #opcion true
            if self.select_option:
                #Selector de niveles
                if self.game_levels.draw(self.display):
                    self.select_option = False
                #Salir del juego
                if self.escape.draw(self.display):
                    self.running = False
            #opcion false
            else: 
                #Mostrar niveles y salida
                self.level_1_portada.draw(self.display)
                self.go_back.draw(self.display)
                #Clickeo de salida
                if self.go_back.clicked:
                    self.select_option = True
                    self.go_back.clicked = False
                #Primer nivel
                if self.first_level == True:
                    pygame.mixer.music.stop()#Detiene la canción
                    pygame.mixer.music.load('.\MUSIC\Melty Blood Type Lumina OST - _Actions in the Lower World.mp3')#Cambia la canción
                    pygame.mixer.music.play(-1)#Reproduce la nueva canción
                    pygame.mixer.music.set_volume(0.5)#Funciona de 0.0 a 1.0
                    if self.level.replay == False:
                        self.level.play()
                    else: 
                        self.level.reset()
                        self.level.play()
                    print(self.level.complete_collection)
                    self.reset() #reseteo de estados
                #Se desbloque luego de agarrar todas las monedas del nivel
                if self.level.complete_collection:
                    self.level_2_portada.draw(self.display)
                    #Segundo nivel
                    if self.second_level == True:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('.\MUSIC\Star Wars VI (The Complete Score) - Into The Death Star.mp3')
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.5)#Funciona de 0.0 a 1.0
                        if self.level_2.replay == False:
                            self.level_2.play()
                        else: 
                            self.level_2.reset()
                            self.level_2.play()
                        self.reset() #reseteo de estados

    #Reseteo de estados opciones
    def reset(self):
        self.first_level = False
        self.second_level = False
        self.select_option = True
        pygame.mixer.music.load('.\MUSIC\Star wars Episode III soundtrack - Battle over Coruscant.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)#Funciona de 0.0 a 1.0
    def render(self):
        pygame.display.flip()
Game().run()