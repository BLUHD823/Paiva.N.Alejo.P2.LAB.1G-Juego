from typing import Any
import pygame, sys 
from pygame.locals import *
from pygame.sprite import Group

class Player(pygame.sprite.Sprite):
    def __init__(self, posicion,velocidad,diccionario,diccionario_girado,gravedad,salto_distancia,life) -> None:
        super().__init__()
        #sprites
        self.sprit_girado = diccionario_girado # {'idle_animation':[4],'walking_animation':[4],''jumping_animation':[2]'}
        self.sprit = diccionario # {'idle_animation':[4],'walking_animation':[4],''jumping_animation':[2]'}
        #superficie
        self.image = diccionario['idle_animation'][0]
        self.rect = self.image.get_rect()
        self.rect.midbottom = posicion
        self.mask = pygame.mask.from_surface(self.image)
        #movimiento
        self.direction = pygame.math.Vector2(0,0)#Vector que me permite ver la dirección
        self.velocidad_x = velocidad#Velocidad de movimientos
        self.gravity = gravedad#Cantidad de gravedad
        self.jump_speed = salto_distancia#Distancia de Salto
        self.direccion = 'RIGHT'
        self.status = 'idle'
        #animacion
        self.frame_index = 0
        self.animation_speed = 0.15
        #estado muerte y vida
        self.invincible = False
        self.invincibility_duration = 600#Duranción de la inmortalidad#
        self.hurt_time = 0#Contador del tiempo después de recibir daño
        self.life = life
    def status_animation(self,display):
        direccion = None
        #Diccionarios de sprites, dependiendo la dirección
        if self.direccion == 'RIGHT':
            direccion = self.sprit
        elif self.direccion == 'LEFT':
            direccion = self.sprit_girado
        #Estados
        if self.direction.y > 0:
            self.status = 'falling'
        if self.direction.y < 0:
            self.status = 'jumping'
        if self.life <= 0:
            self.status = 'death'
        #animación idle
        if self.status == 'idle':
            self.frame_index += self.animation_speed#velocidad de animación
            if self.frame_index >= len(direccion['idle_animation']):
                self.frame_index = 0
            self.image = direccion['idle_animation'][int(self.frame_index)]
            display.blit( self.image,self.rect)
        #animación caminata
        if self.status == 'walking':
            self.frame_index += self.animation_speed
            if self.frame_index >= len(direccion['walking_animation']):
                self.frame_index = 0
            self.image = direccion['walking_animation'][int(self.frame_index)]
            display.blit( self.image,self.rect)
        #animación salto
        if self.status == 'jumping':
            self.frame_index += self.animation_speed
            if self.frame_index >= len(direccion['jumping_animation']):
                self.frame_index = 0
            self.image = direccion['jumping_animation'][int(self.frame_index)]
            display.blit( self.image,self.rect)
        #animación caída
        if self.status == 'falling':
            self.frame_index += self.animation_speed
            if self.frame_index >= len(direccion['falling_animation']):
                self.frame_index = 0
            self.image = direccion['falling_animation'][int(self.frame_index)]
            display.blit( self.image,self.rect)
    #Movimiento izquierda
    def mover_x_izq(self):
        self.direccion = "LEFT"
        self.status = "walking"
        if self.rect.left > 0:
            self.direction.x = -1  
        else:
            self.rect.left = 0   
    #Movimiento derecha
    def mover_x_derecha(self,WIDTH):
        self.direccion = "RIGHT"
        self.status = "walking"
        if self.rect.right < WIDTH:
            self.direction.x = 1        
        else:
            self.rect.right = WIDTH 
    #gravedad  
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    #salto
    def salto(self):
        self.direction.y = self.jump_speed
    #Ser dañado
    def get_damage(self):
        if  self.invincible == False:
            self.invincible = True
            self.hurt_time = pygame.time.get_ticks()#tiempo en milisegundos
            self.life -= 1#pierde una vida al ser atacado
    #Hace que el jugador no sea dañado por cierto tiempo
    def invincibility_timer(self):
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= self.invincibility_duration:#
                self.invincible = False
    #actualiza los sprites
    def update(self,display):
        self.status_animation(display)
        self.rect.x += self.direction.x * self.velocidad_x
        self.invincibility_timer()
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self,dict_l,dict_r,plataforma,velocity,orientacion) -> None:
        super().__init__()
        #sprites
        self.sprites = dict_r
        self.sprites_left = dict_l
        #definir superficie y mascara
        self.surface = self.sprites['walking_animation'][0]
        self.rect = self.surface.get_rect()
        self.rect.midbottom = plataforma.midtop
        self.position = plataforma.midtop
        self.mask = pygame.mask.from_surface(self.surface)
        #movimiento
        self.direction = pygame.math.Vector2(0,0)
        self.velocity = velocity#velocidad
        self.old_velocity = velocity#variable con la velocidad inicial
        self.status = 'walking'
        #animacion
        self.frame_index = 0
        self.animation_speed = 0.15
        self.right_limit = plataforma.topright[0]
        self.left_limit = plataforma.topleft[0]
        self.orientation = orientacion
        self.dead = False
    def animate(self,display):
        #Orientación
        direccion = None
        if self.orientation ==  'right':
            direccion = self.sprites  
        elif self.orientation == 'left':
            direccion = self.sprites_left
        #Estados de animación
        #caminata
        if self.status == 'walking':
            self.frame_index += self.animation_speed
            if self.frame_index >= len(direccion['walking_animation']):
                    self.frame_index = 0
            self.surface = direccion['walking_animation'][int(self.frame_index)]
            display.blit( self.surface,self.rect)
        #muerte
        if self.status == 'death':
            self.frame_index += self.animation_speed
            if self.frame_index >= len(direccion['death_animation']):
                self.frame_index = 0
                self.dead  = True
            self.surface = direccion['death_animation'][int(self.frame_index)]
            display.blit( self.surface,self.rect)
        #ataque
        if self.status == 'attack':
            self.frame_index += self.animation_speed
            if self.frame_index >= len(direccion['attack_animation']):
                self.frame_index = 0
                self.dead = False
                self.velocity = self.old_velocity
            self.surface = direccion['attack_animation'][int(self.frame_index)]
            display.blit( self.surface,self.rect) 
    #Movimiento   
    def move(self):
        if self.orientation == 'right':
            self.rect.x += self.velocity
        if self.orientation == 'left':
            self.rect.x -= self.velocity   
        if self.rect.right >= self.right_limit:
            self.orientation = 'left'
            self.status = 'walking'
        if self.rect.left <= self.left_limit:
            self.orientation = 'right'
            self.status = 'walking'
    #Actualización
    def update(self,display):
        self.move()
        self.animate(display)

class Coins(pygame.sprite.Sprite):
    def __init__(self, posicion,dict,bigger_dict,bool) -> None:
        super().__init__()
        #Sprites y superficie
        self.sprites = dict
        self.bigger_sprites = bigger_dict
        self.surface = self.sprites['animation'][0]
        self.rect = self.surface.get_rect()
        self.position = posicion
        self.rect.midbottom = self.position
        self.mask = pygame.mask.from_surface(self.surface)
        #Animación
        self.frame_index = 0
        self.animation_speed = 0.15
        #Tamaño de sprites
        self.tamaño = bool
    def animate(self):
        if self.tamaño == True:
            diccionario = self.bigger_sprites
        else:
            diccionario = self.sprites
        self.frame_index += self.animation_speed
        if self.frame_index >= len(diccionario['animation']):
                self.frame_index = 0
        self.surface = diccionario['animation'][int(self.frame_index)]
        self.rect = self.surface.get_rect()
        self.rect.midbottom = self.position
    def draw(self,display):
        self.animate()
        display.blit(self.surface, self.rect)

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, posicion,path) -> None:
        super().__init__()
        self.surface = pygame.image.load(path)
        self.rect = self.surface.get_rect()
        self.rect.midbottom = posicion
        self.mask = pygame.mask.from_surface(self.surface)
        self.posicion = posicion
    def draw(self,display):
        display.blit(self.surface, self.rect)
    
    
class Options(pygame.sprite.Sprite):
    def __init__(self,posicion,path) -> None:
        super().__init__()
        self.surface = path
        self.rect = self.surface.get_rect()
        self.rect.midbottom = posicion
        self.mask = pygame.mask.from_surface(self.surface)
        self.clicked = False
        self.click_allowed = True#bandera que desactiva el if inmediatamente después de efectuar el click
    def draw(self,display):
        display.blit(self.surface,self.rect)
        #sacar la posición del mouse
        pos = pygame.mouse.get_pos()
        #acciones del mouse
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and self.click_allowed:
                self.click_allowed = False
                self.clicked = True
                print(self.clicked) 
            if pygame.mouse.get_pressed()[0] == 0:
                self.click_allowed = True
                self.clicked = False

class Texto:
    def __init__(self,font,text_color,x,y) -> None:
        self.count = 0
        self.text = (f"X {self.count}")#Impresión del contador
        self.text_font = font#Fuente de texto
        self.color = text_color#Color
        #Posición
        self.x = x
        self.y = y
    def draw_text(self,display):
        #Actualización
        self.text = (f"X {self.count}")
        img = self.text_font.render(self.text,True,self.color)
        display.blit(img,(self.x,self.y))

class Life(pygame.sprite.Sprite):
    def __init__(self,posicion,path,scale) -> None:
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.midbottom = posicion
        self.mask = pygame.mask.from_surface(self.image)
        self.scale = scale
    def draw(self,display):
        self.image = pygame.transform.scale(self.image,self.scale)#Tamaño
        display.blit(self.image,self.rect)
        
        