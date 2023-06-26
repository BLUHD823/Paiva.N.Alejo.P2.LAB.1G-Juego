import pygame
from pygame.sprite import _Group

class Paleta(pygame.sprite.Sprite):
    
    def __init__(self, posicion,velocidad,diccionario,diccionario_girado,gravedad,salto_distancia) -> None:
        super().__init__()
        self.sprit_girado = diccionario_girado
        self.sprit = diccionario
        self.image = diccionario['idle_animation'][0]
        self.rectangulo = self.image.get_rect()
        self.rectangulo.midbottom = posicion
        self.direction = pygame.math.Vector2(0,0)
        self.velocidad_x = velocidad
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
            self.direction.x = 1       
            self.posicion = self.rectangulo.midbottom
        else:
            self.rectangulo.left = 0
            
        
    def mover_x_derecha(self,WIDTH):
        self.direccion = "RIGHT"
        self.status = "walking"
        if self.rectangulo.right < WIDTH:
            self.direction.x = 1      
            self.posicion = self.rectangulo.midbottom
        else:
            self.rectangulo.right = WIDTH
        
    # def apply_gravity(self,bool):
    #     if bool:
            
    #         self.rectangulo.y += self.gravity
    #         # self.velocidad_y += self.gravity
    #         # self.rectangulo.bottom += self.velocidad_y

    # def salto(self):
    #     self.rectangulo.bottom += self.jump_speed
    #     self.status = 'jumping'
        
            
    # def draw(self,display):
    #     self.get_status(display)
       

    # def update(self,display,tile_set):
        