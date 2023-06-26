import pygame, sys 
from game import Level_1
from assets import Options
from imagenes import menu

class Game():
    def __init__(self) -> None:
        level = Level_1()
        # game.play()

        self.WIDTH = 1280
        self.HEIGHT = 720
        FPS = 60

        self.sprites = menu

        display = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption("MENU")

        fondo = menu['BG']
        game_levels = Options((self.WIDTH // 2, self.HEIGHT - 337),self.sprites['GAME_LEVELS'])
        options = Options((self.WIDTH // 2, self.HEIGHT - 270),self.sprites['OPTIONS'])
        escape = Options((self.WIDTH // 2, self.HEIGHT - 193),self.sprites['QUIT'])

        pygame.init()
        run = True
        while run:
            reloj = pygame.time.Clock()
            reloj.tick(FPS)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT: #QUIT SERÍA LA X DE CERRAR
                    pygame.quit()
                    sys.exit()

            display.blit(fondo,(0,0))

            if game_levels.draw(display):
                level.play()
            options.draw(display)
            if escape.draw(display):
                run = False
            
            pygame.display.flip()

Game()