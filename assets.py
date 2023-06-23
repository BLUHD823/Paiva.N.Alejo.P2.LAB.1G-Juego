import pygame, sys 
from pygame.locals import *



def random_color(lista):
    import random
    indice = random.randrange(0,len(lista))
    return lista[indice]

class Paleta(pygame.sprite.Sprite):
    
    def __init__(self, posicion,velocidad,diccionario,diccionario_girado,gravedad,salto_distancia) -> None:
        # self.image = pygame.image.load("C:\\Users\\Alejo\\Desktop\\pygame\\idle\\idle 1.png")

        # self.image = pygame.transform.scale(self.image,(80,103))
        super().__init__()
        self.sprit_girado = diccionario_girado
        self.sprit = diccionario
        self.image = diccionario['idle_animation'][0]
        self.rectangulo = self.image.get_rect()
        self.rectangulo.midbottom = posicion
        self.velocidad_x = velocidad
        self.velocidad_y = 0
        self.gravity = gravedad
        self.jump_speed = salto_distancia
        self.direccion = 'RIGHT'
        self.status = 'idle'
        self.contador_entero = 0
        self.contador_flotante = 0.0

    def animacion(self,display,lista,diccionario,frames):
            if self.contador_entero >= frames:
                    self.contador_entero = 0
            display.blit(diccionario[lista][self.contador_entero],self.rectangulo)
            if self.contador_flotante == 1.0:
                self.contador_entero += 1
                self.contador_flotante = 0.0    
            else:
                self.contador_flotante += 0.2
                
    
    def get_status(self,display):
        if self.direccion == 'RIGHT':
            if self.status == 'idle':
                lista = 'idle_animation'
                frames = len(self.sprit['idle_animation'])
                dictionary = self.sprit
                
                self.animacion(display,lista,dictionary,frames)
            if self.status == 'walking':
                lista = 'walking_animation'
                frames = len(self.sprit['walking_animation'])
                dictionary = self.sprit
                self.animacion(display,lista,dictionary,frames)
            if self.status == 'jumping':
                lista = 'jumping_animation'
                frames = len(self.sprit['jumping_animation'])
                dictionary = self.sprit
                self.animacion(display,lista,dictionary,frames)
        
        if self.direccion == 'LEFT':
            if self.status == 'idle':
                lista = 'idle_animation'
                frames = len(self.sprit_girado['idle_animation'])
                dictionary = self.sprit_girado
                self.animacion(display,lista,dictionary,frames)    
            if self.status == 'walking':
                lista = 'walking_animation'
                frames = len(self.sprit_girado['walking_animation'])
                dictionary = self.sprit_girado
                self.animacion(display,lista,dictionary,frames)      
            if self.status == 'jumping':
                lista = 'jumping_animation'
                frames = len(self.sprit_girado['jumping_animation'])
                dictionary = self.sprit_girado
                self.animacion(display,lista,dictionary,frames)

    def mover_x_izq(self):
        self.direccion = "LEFT"
        self.status = "walking"
        if self.rectangulo.left > 0:
            self.rectangulo.left  -= self.velocidad_x      
            self.posicion = self.rectangulo.midbottom
        else:
            self.rectangulo.left = 0
            
        
    def mover_x_derecha(self,WIDTH):
        self.direccion = "RIGHT"
        self.status = "walking"
        if self.rectangulo.right < WIDTH:
            self.rectangulo.right  += self.velocidad_x      
            self.posicion = self.rectangulo.midbottom
        else:
            self.rectangulo.right = WIDTH
        
    def apply_gravity(self,bool):
        if bool:
            
            self.rectangulo.y += self.gravity
            # self.velocidad_y += self.gravity
            # self.rectangulo.bottom += self.velocidad_y

    def salto(self):
        self.rectangulo.bottom += self.jump_speed
        self.status = 'jumping'
        # self.direccion.y += self.jump_speed
            
    def draw(self,display):
        self.get_status(display)
        # display.blit(self.image,self.rectangulo)

    def update(self,display,tile_set):
        self.draw(display)
        if self.gravity == True:
            self.status = 'jumping'
        self.apply_gravity(True)
        
        if self.rectangulo.colliderect(tile_set):
            self.rectangulo.bottom = tile_set.rect.top 
            self.status = 'idle'
            self.apply_gravity(False)
            
        
            
        
class Obstaculo:
    def __init__(self,posicion) -> None:
        self.surface = pygame.image.load('.\src\obstacul0.png')
        self.rect = self.surface.get_rect()
        self.rect.bottomleft = posicion
        self.posicion = posicion
    
class Piso:
    def __init__(self,posicion) -> None:
        self.surface = pygame.image.load('./src/tile definitivo.png')
        self.rect = self.surface.get_rect()
        self.rect.bottomleft = posicion
        self.posicion = posicion