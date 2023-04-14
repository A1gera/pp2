import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((600, 360))
pygame.display.set_caption("MyGame")
icon = pygame.image.load('practice/images/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('practice/images/bg.jpeg')
# player= pygame.image.load('practice/images/left.png')

walk_right = [
    pygame.image.load('practice/images/right.png'),
    pygame.image.load('practice/images/right2.png'),
    pygame.image.load('practice/images/right3.png'),
    pygame.image.load('practice/images/right4.png')
]
walk_left = [
    pygame.image.load('practice/images/left.png'),
    pygame.image.load('practice/images/left2.png'),
    pygame.image.load('practice/images/left3.png'),
    pygame.image.load('practice/images/left4.png')
]

player_anim_count = 0
# myFont = pygame.font.Font('practice/Abs/dyna.ttf', 40)
# text_surface = myFont.render('U knoooow', False, 'White')
# square = pygame.Surface((50, ))
# square.fill('Blue')
bg_x = 0

player_speed = 5
player_x = 150
player_y = 205
isJump = False
jump_count = 7

bg_sound = pygame.mixer.Sound('practice/sounds/bg.mp3')
bg_sound.play()

done = False
while not done:
    
    #можно написать вместо скрин другой обьект тоже
    # pygame.draw.circle(screen, 'Red', (250,150), 30)
    # screen.blit(text_surface, (200,120))
    keys = pygame.key.get_pressed()
    
    screen.blit(bg,(bg_x,0))
    screen.blit(bg,(bg_x + 600,0))
    
    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x,player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x,player_y))
    
    
    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -=player_speed
    elif keys[pygame.K_RIGHT] and player_x < 200:
        player_x +=player_speed
    
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
                   
            jump_count -=1
        else:
            isJump = False
            jump_count = 7
    
    
    
    
    if player_anim_count == 3:
        player_anim_count =0
    else:
        player_anim_count += 1
    
    bg_x -=2
    if bg_x == -600:
        bg_x = 0
    
    # screen.blit(square, (0,0))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            
            
    clock.tick(15)
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a:
        #         screen.fill((121, 171, 252))