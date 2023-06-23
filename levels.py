from pygame.locals import *
from assets import *
#player.rectangulo.bottom > obstaculo.rect.top and player.rectangulo.top < obstaculo.rect.top

def colision_v(player,obstaculo):
    if player.rectangulo.colliderect(obstaculo):
        if player.direccion == "RIGHT" and not( player.rectangulo.top < obstaculo.rect.top):
            player.rectangulo.right = obstaculo.rect.left
        elif player.direccion == "LEFT"  and not( player.rectangulo.top < obstaculo.rect.top):
            player.rectangulo.left = obstaculo.rect.right
        
        if  player.rectangulo.top < obstaculo.rect.top:
            player.rectangulo.bottom = obstaculo.rect.top
            
        # elif player.rectangulo.top < obstaculo.rect.bottom and player.rectangulo.bottom > obstaculo.rect.bottom:
        #     player.rectangulo.top = obstaculo.rect.bottom
