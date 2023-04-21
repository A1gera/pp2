import pygame
import os
import math
from datetime import datetime

pygame.init()
width = 800
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mickey so fun clock')
clock_img = pygame.image.load('lab7/clockA/clock.png')
min_hand_img = pygame.image.load('lab7/clockA/secondsHand.png')
sec_hand_img = pygame.image.load('lab7/clockA/minuteHand.png')

def get_time():
    now = datetime.now()
    min = now.minute
    sec = now.second
    return min, sec

def rotate_hand(hand_img, angle):
    rotated_img = pygame.transform.rotate(hand_img, angle)
    rect = rotated_img.get_rect(center=hand_img.get_rect().center)
    return rotated_img, rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    min, sec = get_time()

    min_angle = min * -6 
    sec_angle = sec * -6 

    min_hand_rotated, min_hand_rect = rotate_hand(min_hand_img, min_angle)
    sec_hand_rotated, sec_hand_rect = rotate_hand(sec_hand_img, sec_angle)
    clock_img = pygame.transform.scale(clock_img, (800, 800))
    screen.blit(clock_img, (0, 0))

    min_hand_x = 400 - min_hand_rect.width / 2
    min_hand_y = 400 - min_hand_rect.height / 2
    screen.blit(min_hand_rotated, (min_hand_x, min_hand_y))

    sec_hand_x = 400 - sec_hand_rect.width / 2
    sec_hand_y = 400 - sec_hand_rect.height / 2
    screen.blit(sec_hand_rotated, (sec_hand_x, sec_hand_y))







    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(60)