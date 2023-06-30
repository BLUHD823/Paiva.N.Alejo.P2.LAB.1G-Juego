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
        if player.direction.y > 0:  # top
            player.rect.bottom = sprite.rect.top
            player.direction.y = 0
        elif player.direction.y < 0:  # bottom
            player.rect.top = sprite.rect.bottom

def colision_enemy(player,enemies,health):
    
    enemy_collision = pygame.sprite.spritecollide(player,enemies,False,pygame.sprite.collide_mask)
    for enemy in enemy_collision:
        if player.direction.y > 0 and player.rect.bottom < enemy.rect.centery:#Matar enemigos
            enemy.status = 'death'
            enemy.velocity = 0
            player.direction.y = -10
            if enemy.dead:
                enemy.kill()#Elimina al enemigo del grupo
        else: 
            #ataque enemigo derecha
            if player.direccion == 'LEFT':
                enemy.orientation = 'right'
                enemy.status = 'attack'
                player.get_damage()
                if player.life < len(health):
                    health.sprites()[-1].kill()  # Elimina el último corazón del grupo
            #ataque enemigo izquierda
            elif player.direccion == 'RIGHT' :
                enemy.orientation = 'left'
                enemy.status = 'attack'
                player.get_damage()
                if player.life < len(health):
                    health.sprites()[-1].kill()  # Elimina el último corazón del grupo

def collect_coins(player,coins,counter):
    coins_collision = pygame.sprite.spritecollide(player,coins,False,pygame.sprite.collide_mask)
    #En caso de colisión elimina monedas del grupo
    for coin in coins_collision:
        coin.kill()
        #contador de monedas recolectadas
        counter.count += 1#contador del texto
        print(counter.count)


    



        
        




            


