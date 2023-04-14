import random
import pygame
import time
pygame.init()
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
#SETUP FONTS
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
                x=WIDTH // BLOCK_SIZE // 2,
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
                BLOCK_SIZE,
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
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y

        self.body[0].x += dx
        self.body[0].y += dy

        if self.body[0].x > WIDTH // BLOCK_SIZE:
            pygame.quit()
        elif self.body[0].x < 0:
            pygame.quit()
        elif self.body[0].y < 0:
            pygame.quit()
        elif self.body[0].y > HEIGHT // BLOCK_SIZE:
            pygame.quit()
        for block in self.body[2:]:
            if block.x == self.body[0].x and block.y == self.body[0].y:
                pygame.quit()
        if not running:
            pygame.quit()
    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)

class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            GREEN,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
def generate_random_food(snake):
    while True:
        x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
        y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
        if not any(block.x == x and block.y == y for block in snake.body):
            return Point(x, y)

snake = Snake()
food = Food(5, 5)
dx, dy = 0, 0
running = True

while running:
    SCREEN.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN:
                dx, dy = 0, +1
            elif event.key == pygame.K_RIGHT:
                dx, dy = 1, 0
            elif event.key == pygame.K_LEFT:
                dx, dy = -1, 0

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
        pygame.time.delay(1000)

    snake.move(dx, dy)
    if snake.check_collision(food):
        SCORE+=1
        snake.body.append(
            Point(snake.body[-1].x, snake.body[-1].y)
        )
        food.location = generate_random_food(snake)

    snake.draw()
    food.draw()
    draw_grid()
    scores = font_small.render(str(SCORE), True, WHITE)
    SCREEN.blit(scores,(2,10))
    levels = font_small.render(str(f"LEVEL:{LEVEL}"),True,WHITE)
    SCREEN.blit(levels, (700,10))
    pygame.display.flip()
    clock.tick(FPS)