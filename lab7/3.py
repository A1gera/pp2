import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

done = False
x = 80
y = 80
color = (255, 0, 0)
clock = pygame.time.Clock()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] : y -= 20
        if pressed[pygame.K_DOWN] : y += 20
        if pressed[pygame.K_LEFT] : x -= 20
        if pressed[pygame.K_RIGHT] : x += 20
        if x < 20: x = 25
        if x > 790: x = 775
        if y < 10: y = 25
        if y > 590: y = 575
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, color,(x,y), 25)
        
        pygame.display.flip()
        clock.tick(60)