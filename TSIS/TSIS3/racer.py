import pygame
import random

WIDTH, HEIGHT = 400, 600

LANES = [80, 160, 240]

class Player:
    def __init__(self):
        self.lane = 1
        self.x = LANES[self.lane]
        self.y = 500
        self.speed = 5
        self.shield = False
        self.nitro = 0

    def move_left(self):
        if self.lane > 0:
            self.lane -= 1
            self.x = LANES[self.lane]

    def move_right(self):
        if self.lane < 2:
            self.lane += 1
            self.x = LANES[self.lane]


class Enemy:
    def __init__(self, speed):
        self.lane = random.randint(0, 2)
        self.x = LANES[self.lane]
        self.y = -100
        self.speed = speed

    def update(self):
        self.y += self.speed
        

class PowerUp:
    def __init__(self, type):
        self.type = type
        self.lane = random.randint(0, 2)
        self.x = LANES[self.lane]
        self.y = -100
        self.speed = 4