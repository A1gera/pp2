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
# pencil= pygame.image.load("lab8/paint/pencil.png")
# pencil= pygame.transform.scale(pencil, (pencil.get_width()//3 ,pencil.get_height()//3))

class Button(pygame.sprite.Sprite):
    def __init__(self, flag, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.flag = flag
        if flag == 0:
            self.img = pygame.Surface((70, 70)) 
            self.color = img
            self.img.fill(self.color)#если флаг 0 то сплошной цвет
        elif self.flag == 2: # RECT
            self.img = pygame.Surface((70, 70))
            self.img.fill((255, 255, 255))
            pygame.draw.rect(self.img, (0, 0, 0), (10, 20, 50, 35), 2)#х, у, ширина, высота
        elif self.flag == 3: # CIRCLE
            self.img = pygame.Surface((70, 70))
            self.img.fill((255, 255, 255))
            pygame.draw.circle(self.img, (0, 0, 0), (35, 35), 20, 2)#центрб радиус, толщина
        else:
            self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.img, self.rect)

    def check(self, tuple):
        #если все точки находятся в пределах кнопки
        if self.rect.left < tuple[0] < self.rect.right and self.rect.top < tuple[1] < self.rect.bottom:
            return True
        return False

pencil = Button(1, "lab8/paint/pencil.png", 820, 300)#1 - рисование
eraser = Button(1, "lab8/paint/eraser.png", 820, 50)
rec = Button(2, None, 820, 280)
cir = Button(3, None, 910, 280)

buttons = pygame.sprite.Group()

buttons.add(Button(0, (0,0,0), 820, 720))
buttons.add(Button(0, (255,0,0), 910, 720))
buttons.add(Button(0, (0,255,0), 910, 660))
buttons.add(Button(0, (0,0,255), 820, 660))

buttons.add(cir)
buttons.add(rec)
buttons.add(eraser)
buttons.add(pencil)

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
                    if flag == 0:#pencil
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
                pygame.draw.line(screen, color, prev, cur, 5)# нач, конеч, ширина
                #проверка, сохранена ли предыдущая позиция мыши в переменной prev. Если он существует, то рисуется линия
                prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
    
    elif flag == 2:
        if event.type == pygame.MOUSEBUTTONUP:
            cur = pygame.mouse.get_pos()
            if prev:     
                #вычисляют верхний левый угол прямоугольника, а abs вычислить его ширину и высоту
                pygame.draw.rect(screen, color, (min(prev[0], cur[0]), min(prev[1], cur[1]), abs(prev[0] - cur[0]), abs(prev[1] - cur[1])), 2)
                prev = cur
    
    elif flag == 3:
        if event.type == pygame.MOUSEBUTTONUP:
            cur = pygame.mouse.get_pos()
            if prev:     
                #половина между нач и кон точкамиб радиус
                pygame.draw.circle(screen, color, (min(prev[0], cur[0]) + abs(prev[0] - cur[0])//2, min(prev[1], cur[1]) + abs(prev[1] - cur[1])//2), abs(prev[0] - cur[0])//2, 2)
                prev = cur

    screen.blit(menu, (800, 0)) #расположение цвета меню
    for button in buttons:
        button.draw()
    pygame.display.flip()
    clock.tick(60)