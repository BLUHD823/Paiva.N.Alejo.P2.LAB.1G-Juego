from pygame.locals import *
from assets import *
from imagenes import *
#player.rectangulo.bottom > obstaculo.rect.top and player.rectangulo.top < obstaculo.rect.top

def colision_v(player,group):
    colisiones = pygame.sprite.spritecollide(player, group, False,pygame.sprite.collide_mask)
    for sprite in colisiones:
        if player.direction.x < 0: #left
            player.rect.left = sprite.rect.right
        elif player.direction.x > 0: #right
            player.rect.right = sprite.rect.left

def colision_h(player,group):
    player.apply_gravity()
    colisiones = pygame.sprite.spritecollide(player, group, False,pygame.sprite.collide_mask)
    for sprite in colisiones:
        if player.direction.y > 0:  # left
            player.rect.bottom = sprite.rect.top
            player.direction.y = 0
            
        elif player.direction.y < 0:  # right
            player.rect.top = sprite.rect.bottom
            player.direction.y = 0

def colision_enemy(player,enemies):
    
    enemy_collision = pygame.sprite.spritecollide(player,enemies,False,pygame.sprite.collide_mask)
    
    for enemy in enemy_collision:
        # old_velocity = enemy.velocity
        if player.direction.y > 0 and player.rect.bottom < enemy.rect.centery:
            enemy.status = 'death'
            enemy.velocity = 0
            player.salto()
            if enemy.dead:
                enemy.kill()
        else: 
            enemy.status = 'attack'
            if enemy.orientation == 'right':
                player.rect.x += 100
                player.direction.y = -12
            else:
                player.rect.x += -100
                player.direction.y = -12
            player.get_damage()
            
                
            


