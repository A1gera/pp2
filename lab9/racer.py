#Imports
import pygame, sys
import random, time
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

#COLORS
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


width = 400
height = 600
speed = 5
score = 0
coin = 0
coin_num = 0

#FONT and BACKGROUND 
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("GAME OVER", True, BLACK)

background = pygame.image.load("lab8/racer/AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
#CAPTION
pygame.display.set_caption("Racer")

#CREATING AN ENEMY AND HIS MOVE
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/racer/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40),0)
        
      def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width-40),0)

#CREATING A PLAYER AND HIS MOVE
class Player(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/racer/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
      def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)

#CREATING A COIN CLASS        
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/racer/coin.png")
        self.image = pygame.transform.scale(pygame.image.load('lab8/racer/coin.png'), (70,70))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40),0)
        
      def move(self):
        global coin
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, width-40),0)
            
class Coin2(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/racer/pinkcoin.png")
        self.image = pygame.transform.scale(pygame.image.load('lab8/racer/pinkcoin.png'), (60,60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40),0)
        
      def move(self):
        global coin
        self.rect.move_ip(0,speed+1)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(100, 400 ),0)
       
                         
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin2()

#MAKING GROUPS BY SPRITE
enemies = pygame.sprite.Group()
enemies.add(E1)
loot = pygame.sprite.Group()
loot.add(C1)
loot2 = pygame.sprite.Group()
loot2.add(C2)
allsprites = pygame.sprite.Group()
allsprites.add(P1)
allsprites.add(E1)
allsprites.add(C1)
allsprites.add(C2)
incr_speed = pygame.USEREVENT + 1
pygame.time.set_timer(incr_speed, 1000)

#THE GAME SETTINGS
while True:
    for event in pygame.event.get():
        if event.type == incr_speed:
            speed += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(score), True, BLACK)
    coins = font_small.render(str(coin), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coins, (width-30, 10))
        
    for entity in allsprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()
    
    #CHECKING THE COLLISION OF PLAYER AND COIN        
    if pygame.sprite.spritecollideany(P1, loot):
            pygame.mixer.Sound('lab8/racer/coin.wav').play()
            coin += 1
            coin_num += 1
            C1.rect.top = 0
            C1.rect.center = (random.randint(40, width-40),0)
            
    #CHECKING THE COLLISION OF PLAYER AND ENEMY        
    if pygame.sprite.spritecollideany(P1, loot2):
            pygame.mixer.Sound("lab8/racer/coin.wav").play()
            coin += 3
            coin_num += 3
            C2.rect.top = 0
            C2.rect.center = (random.randint(40, width-40),0)
            
    if coin_num >= 10:
      coin_num = 0
      speed+=1
            
    if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.Sound('lab8/racer/crash.wav').play()
            time.sleep(1)
            
            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30,250))
            
            pygame.display.update()
            for entity in allsprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    FramePerSec.tick(FPS)
