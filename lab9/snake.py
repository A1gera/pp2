import random
import pygame
import time
pygame.init()
counter = 0
WIDTH, HEIGHT = 800, 800
FPS = 5
SCORE = 1
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
#COLORS
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
#FONTS
direction = None
font_small = pygame.font.SysFont("Verdana",20)
font = pygame.font.SysFont("Verdana",60)

clock = pygame.time.Clock()
LEVEL = 1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,#разделили на сетку, потом на вторую половинку поставили
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,#ограничения для головы змеи
            )
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,#вторая часть змейки
                )
            )

    def move(self, dx, dy):
        for idx in range(len(self.body) - 1, 0, -1):# начиная с полседнего до второго,размер шага -1
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y#перемещает тело запоминая положение предыдущего

        self.body[0].x += dx#добавляет к голове следующую координату
        self.body[0].y += dy

        #если вышла за рамки
        if self.body[0].x > WIDTH // BLOCK_SIZE - 1:
            pygame.quit()
        elif self.body[0].x < 0:
            pygame.quit()
        elif self.body[0].y < 0:
            pygame.quit()
        elif self.body[0].y > HEIGHT // BLOCK_SIZE - 1:
            pygame.quit()
            #ecли голова столкнется со своим телом
        for block in self.body[2:]:
            if block.x == self.body[0].x and block.y == self.body[0].y:
                pygame.quit()
        if not running:
            pygame.quit()
    def check_collision(self, food):
        if food.foodtype == 1:
            if food.location.x != self.body[0].x:
                return False
            if food.location.y != self.body[0].y:
                return False
            return True
        else:
            if food.location.x == self.body[0].x - 1 and food.location.y == self.body[0].y:# сьела ли она ее(ушла внутрь)
                return True
            if food.location.x == self.body[0].x and food.location.y == self.body[0].y - 1:
                return True
            if food.location.x != self.body[0].x: 
                return False
            if food.location.y != self.body[0].y:
                return False
            # print("->",food.location.x)
            # print("->",food.location.y)
            # return True
#сетка
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)

class Food:
    def __init__(self, x, y, foodtype):
        self.location = Point(x, y)
        self.foodtype = foodtype 

    def draw(self):
        if self.foodtype == 1:
            pygame.draw.rect(
                SCREEN,
                GREEN,
                pygame.Rect(
                    self.location.x * BLOCK_SIZE,
                    self.location.y * BLOCK_SIZE,
                    BLOCK_SIZE,#ширина
                    BLOCK_SIZE #высота
                )
            )
        else:
            pygame.draw.rect(
                SCREEN,
                RED,
                pygame.Rect(
                    (self.location.x * BLOCK_SIZE),
                    (self.location.y * BLOCK_SIZE),
                    BLOCK_SIZE * 2,
                    BLOCK_SIZE * 2
                )
            )
def generate_random_food(snake):
    while True:
        x = random.randint(0, WIDTH // BLOCK_SIZE - 2)
        y = random.randint(0, HEIGHT // BLOCK_SIZE - 2)
        if not any(block.x == x and block.y == y for block in snake.body):#если там есть змея, то новая точка
            return Point(x, y)

snake = Snake()
food = Food(5, 5,random.randint(1,2))#положение 5 и 5, фуд типа 1 и 2
dx, dy = 0, 0
running = True
LIFEMOMENT = pygame.USEREVENT + 1
pygame.time.set_timer(LIFEMOMENT, 1000)
while running:
    SCREEN.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 2:#2 down, 4 up
                direction = 4
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN and direction != 4:
                dx, dy = 0, +1
                direction = 2
            elif event.key == pygame.K_RIGHT and direction != 3:#3left, 1 right
                dx, dy = 1, 0
                direction = 1
            elif event.key == pygame.K_LEFT and direction != 1:
                dx, dy = -1, 0
                direction = 3
        if event.type == LIFEMOMENT:
            counter+=1
            if counter == 5:
                food.location = generate_random_food(snake)
                food.foodtype = random.randint(1,2)
                counter = 0


    if SCORE == 5 and LEVEL<2:
        LEVEL+=1
        FPS+=5
        text = font.render("LEVEL UP!",True,WHITE)
        SCREEN.blit(text, (250,340))
        pygame.display.update()
        pygame.time.delay(1000)
    elif SCORE == 10 and LEVEL<3:
        LEVEL+=1
        FPS+=5
        text = font.render("LEVEL UP!",True,WHITE)
        SCREEN.blit(text, (250,340))
        pygame.display.update()
        pygame.time.delay(1000)#приостановитт на 1 секунду

    snake.move(dx, dy)
    # print(snake.body[0].x)
    # print(snake.body[0].y)
    if snake.check_collision(food):
        if food.foodtype == 1:
            SCORE+=1
            snake.body.append(
                Point(snake.body[-1].x, snake.body[-1].y)
            )
        else:
            SCORE+=2
            snake.body.append(
                Point(snake.body[-1].x, snake.body[-1].y)
            )
            snake.body.append(
                Point(snake.body[-1].x, snake.body[-1].y)
            )
        food.location = generate_random_food(snake)
        food.foodtype = random.randint(1,2)

    snake.draw()
    food.draw()
    draw_grid()
    scores = font_small.render(str(SCORE), True, WHITE)
    SCREEN.blit(scores,(2,10))
    levels = font_small.render(str(f"LEVEL:{LEVEL}"),True,WHITE)
    SCREEN.blit(levels, (700,10))
    pygame.display.flip()
    clock.tick(FPS)