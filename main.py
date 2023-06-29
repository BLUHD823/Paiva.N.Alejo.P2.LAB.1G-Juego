import pygame, sys 
from game import Level_1
from assets import Options
from imagenes import menu

class Game():
    def __init__(self) -> None:
        self.level = Level_1()
        # game.play()

        self.WIDTH = 1280
        self.HEIGHT = 720
        self.FPS = 60

        self.sprites = menu

        self.display = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption("MENU")

        self.fondo = menu['BG']
        self.game_levels = Options((self.WIDTH // 2, self.HEIGHT - 337),self.sprites['GAME_LEVELS'])
        self.options = Options((self.WIDTH // 2, self.HEIGHT - 270),self.sprites['OPTIONS'])
        self.escape = Options((self.WIDTH // 2, self.HEIGHT - 193),self.sprites['QUIT'])
        self.level_1_portada =  Options((self.WIDTH // 2, 450),self.sprites['PORTADA_1'])
        

        pygame.init()
        self.select_option =  True
        self.first_level = False
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

    def update(self):
            self.display.blit(self.fondo,(0,0))
            if self.select_option == True:
                if self.game_levels.draw(self.display):
                    self.select_option = False
                self.options.draw(self.display)
                if self.escape.draw(self.display):
                    self.running = False
            elif self.select_option == False: 
                self.level_1_portada.draw(self.display)
                if self.first_level == True:
                    if self.level.replay == False:
                        self.level.play()
                    else: 
                        self.level.reset()
                        self.level.play()
                    self.reset()
    def reset(self):
        self.first_level = False
        self.select_option = True
    def render(self):
        pygame.display.flip()
Game().run()