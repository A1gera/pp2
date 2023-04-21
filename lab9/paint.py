import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 800))
screen.fill('white')
clock = pygame.time.Clock()
menu = pygame.Surface((200, 800))
menu.fill((255, 220, 255))

flag = 1
color = 'black'

class Button(pygame.sprite.Sprite):
    def __init__(self, flag, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.flag = flag
        if flag == 0:
            self.img = pygame.Surface((70, 70)) 
            self.color = img
            self.img.fill(self.color)
        elif self.flag == 2: # RECT
            self.img = pygame.Surface((70, 70))
            self.img.fill((255, 255, 255))
            pygame.draw.rect(self.img, (0, 0, 0), (10, 20, 50, 35), 2)
        elif self.flag == 3: # CIRCLE
            self.img = pygame.Surface((70, 70))
            self.img.fill((255, 255, 255))
            pygame.draw.circle(self.img, (0, 0, 0), (35, 35), 20, 2)
        elif self.flag == 4: # квадр
            self.img = pygame.Surface((70, 70))
            self.img.fill((255, 255, 255))
            pygame.draw.rect(self.img, (0, 0, 0), (15, 15, 40, 40), 2)
        elif self.flag == 5: # прав треуг
            self.img = pygame.Surface((70, 70))
            self.img.fill((255, 255, 255))
            pygame.draw.polygon(self.img, (0, 0, 0), [(15, 15), (15, 50), (50, 50)], 2)
        elif self.flag == 6: # равносторонний
            self.img = pygame.Surface((70, 70))
            self.img.fill((255, 255, 255))
            pygame.draw.polygon(self.img, (0, 0, 0), [(15, 55), (35, 15), (55, 55)], 2)
        elif self.flag == 7: # ромб
            self.img = pygame.Surface((70, 70))
            self.img.fill((255, 255, 255))
            pygame.draw.polygon(self.img, (0, 0, 0), [(15, 35), (35, 15), (55, 35), (35, 55)], 2)
        else:
            self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.img, self.rect)

    def check(self, tuple):
        if self.rect.left < tuple[0] < self.rect.right and self.rect.top < tuple[1] < self.rect.bottom:
            return True
        return False


pencil = Button(1, "lab8/paint/pencil.png", 850, 0)
eraser = Button(1, "lab8/paint/eraser.png", 820, 0)
rec = Button(2, None, 820, 330)
cir = Button(3, None, 910, 330)
sqr = Button(4, None, 820, 440)
rtr = Button(5, None, 910, 440)
etr = Button(6, None, 820, 550)
rho = Button(7, None, 910, 550)

buttons = pygame.sprite.Group()

buttons.add(Button(0, (0,0,0), 820, 720))
buttons.add(Button(0, (255,0,0), 910, 720))
buttons.add(Button(0, (0,255,0), 910, 660))
buttons.add(Button(0, (0,0,255), 820, 660))

buttons.add(cir)
buttons.add(rec)
buttons.add(eraser)
buttons.add(pencil)
buttons.add(sqr)
buttons.add(rtr)
buttons.add(etr)
buttons.add(rho)

prev, cur = None, None

while True:
  
  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        prev = pygame.mouse.get_pos()
        if 799 < prev[0] < 1001:
            for button in buttons:
                if button.check(prev):
                    flag = button.flag
                    if flag == 0:
                        flag = 1
                        color = button.color
                    elif flag == 1:
                        if button == eraser: 
                            color = 'white'
                    break
    if flag == 1:
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
            if prev:     
                pygame.draw.line(screen, color, prev, cur, 5)
                prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
    
    elif flag == 2:
        if event.type == pygame.MOUSEBUTTONUP:
            cur = pygame.mouse.get_pos()
            if prev:     
                pygame.draw.rect(screen, color, (min(prev[0], cur[0]), min(prev[1], cur[1]), abs(prev[0] - cur[0]), abs(prev[1] - cur[1])), 2)
                prev = cur
    
    elif flag == 3:
        if event.type == pygame.MOUSEBUTTONUP:
            cur = pygame.mouse.get_pos()
            if prev:     
                pygame.draw.circle(screen, color, (min(prev[0], cur[0]) + abs(prev[0] - cur[0])//2, min(prev[1], cur[1]) + abs(prev[1] - cur[1])//2), abs(prev[0] - cur[0])//2, 2)
                prev = cur
    elif flag == 4:
        if event.type == pygame.MOUSEBUTTONUP:
            cur = pygame.mouse.get_pos()
            if prev:     
                a = min(abs(prev[0] - cur[0]), abs(prev[1] - cur[1]))
                pygame.draw.rect(screen, color, (min(prev[0], cur[0]), min(prev[1], cur[1]), a, a), 2)
                prev = cur
    elif flag == 5:
        if event.type == pygame.MOUSEBUTTONUP:
            cur = pygame.mouse.get_pos()
            if prev:     
                pygame.draw.polygon(screen, color, [(prev[0], prev[1]), (prev[0], cur[1]), (cur[0], prev[1])], 2)
                prev = cur
    elif flag == 6:
        if event.type == pygame.MOUSEBUTTONUP:
            cur = pygame.mouse.get_pos()
            if prev:     
                a = (cur[1]-prev[1])/(3**0.5)#высота треуг
                pygame.draw.polygon(screen, color, [(prev[0], prev[1]), (prev[0] + a, prev[1] - (prev[1] - cur[1])), (prev[0] + 2*a, prev[1])], 2)
                prev = cur
    elif flag == 7:
        if event.type == pygame.MOUSEBUTTONUP:
            cur = pygame.mouse.get_pos()
            if prev:     
                a = min(prev[1], cur[1])+abs(prev[1]-cur[1])/2#centers
                b = min(prev[0], cur[0])+abs(prev[0]-cur[0])/2
                #Координата x b равна минимуму координаты x prev и cur
                #плюс половина абсолютной разницы между их координатами x.
                pygame.draw.polygon(screen, color, [(prev[0], a), (b, cur[1]), (cur[0], a), (b, prev[1])], 2)
                prev = cur
    screen.blit(menu, (800, 0))
    for button in buttons:
        button.draw()
    pygame.display.flip()
    clock.tick(60)