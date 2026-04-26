import pygame
import random
import json
from config import *
from db import *

class SnakeGame:
    def __init__(self, username):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.username = username
        self.player_id = get_or_create_player(username)
        self.best_score = get_best_score(self.player_id)

        self.load_settings()

        self.reset()

    def load_settings(self):
        with open("settings.json") as f:
            self.settings = json.load(f)

    def reset(self):
        self.snake = [(100, 100)]
        self.direction = (CELL_SIZE, 0)

        self.food = self.spawn_food()
        self.poison = self.spawn_food()
        self.powerup = None

        self.obstacles = []
        self.score = 0
        self.level = 1
        self.speed = FPS_BASE

        self.shield = False
        self.last_power_time = 0

    def spawn_food(self):
        return (
            random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
            random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE
        )

    def spawn_obstacles(self):
        self.obstacles = []
        for _ in range(self.level * 3):
            self.obstacles.append(self.spawn_food())

    def run(self):
        running = True

        while running:
            self.clock.tick(self.speed)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.move_snake()
            self.check_collisions()
            self.draw()

        self.game_over()

    def move_snake(self):
        head_x, head_y = self.snake[0]
        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)
        self.snake.insert(0, new_head)
        self.snake.pop()

    def check_collisions(self):
        head = self.snake[0]

        # walls
        if head[0] < 0 or head[1] < 0 or head[0] >= WIDTH or head[1] >= HEIGHT:
            self.game_over()

        # self
        if head in self.snake[1:]:
            self.game_over()

        # obstacle
        if head in self.obstacles:
            self.game_over()

        # food
        if head == self.food:
            self.score += 1
            self.snake.append(self.snake[-1])
            self.food = self.spawn_food()

            if self.score % 5 == 0:
                self.level += 1
                self.speed += 2

                if self.level >= 3:
                    self.spawn_obstacles()

        # poison
        if head == self.poison:
            self.snake = self.snake[:-2]
            if len(self.snake) <= 1:
                self.game_over()
            self.poison = self.spawn_food()

        # powerup expire
        if self.powerup and pygame.time.get_ticks() - self.last_power_time > 8000:
            self.powerup = None

    def draw(self):
        self.screen.fill((0, 0, 0))

        # snake
        color = self.settings["snake_color"]
        for s in self.snake:
            pygame.draw.rect(self.screen, color, (*s, CELL_SIZE, CELL_SIZE))

        # food
        pygame.draw.rect(self.screen, (255, 255, 0), (*self.food, CELL_SIZE, CELL_SIZE))

        # poison
        pygame.draw.rect(self.screen, (139, 0, 0), (*self.poison, CELL_SIZE, CELL_SIZE))

        # obstacles
        for o in self.obstacles:
            pygame.draw.rect(self.screen, (100, 100, 100), (*o, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()

    def game_over(self):
        save_game(self.player_id, self.score, self.level)
        print("Game Over")
        pygame.quit()
        exit()