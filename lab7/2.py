import pygame
pygame.init()

screen = pygame.display.set_mode((360, 360))
done = False
bg = pygame.image.load('lab7/playerA/player.png')

player = [pygame.mixer.Sound('lab7/playerA/DoIwannaKnow.mp3'), pygame.mixer.Sound('lab7/playerA/church.mp3'), pygame.mixer.Sound('lab7/playerA/heaven.mp3'), pygame.mixer.Sound('lab7/playerA/tuimedaq.mp3'), pygame.mixer.Sound('lab7/playerA/suyemin.mp3')]
i = 0

check = False
stop = True
while not done:
        
        screen.fill((121, 226, 252))
        screen.blit(bg,(0,0))
        pygame.display.update()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                elif event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_SPACE: 
                            player[i].play()
                      elif event.key == pygame.K_ESCAPE:
                            check = False
                            player[i].stop()
                            i = 0
                      elif event.key == pygame.K_RIGHT:
                            player[i].stop()
                            i = (i+1) % len(player)
                            player[i].play()
                      elif event.key == pygame.K_LEFT:
                            player[i].stop()
                            i = (i-1) % len(player)
                            player[i].play()
        
        pygame.display.flip()