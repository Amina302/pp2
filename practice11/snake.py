import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Practice 11")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

snake_block = 20
snake_speed = 10

snake_x = WIDTH // 2
snake_y = HEIGHT // 2

dx = 0
dy = 0

snake_body = []
length = 1

def spawn_food():
    return {
        "x": random.randrange(0, WIDTH, snake_block),
        "y": random.randrange(0, HEIGHT, snake_block),
        "weight": random.choice([1, 2, 3]),
        "spawn_time": pygame.time.get_ticks()
    }

food = spawn_food()

score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and dx == 0:
                dx = -snake_block
                dy = 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx = snake_block
                dy = 0
            elif event.key == pygame.K_UP and dy == 0:
                dx = 0
                dy = -snake_block
            elif event.key == pygame.K_DOWN and dy == 0:
                dx = 0
                dy = snake_block

    snake_x += dx
    snake_y += dy

    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        print("Game Over! Score:", score)
        running = False

    head = [snake_x, snake_y]
    snake_body.append(head)

    if len(snake_body) > length:
        del snake_body[0]

    for block in snake_body[:-1]:
        if block == head:
            print("Game Over! Score:", score)
            running = False

    for block in snake_body:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], snake_block, snake_block))

    current_time = pygame.time.get_ticks()
    if current_time - food["spawn_time"] > 5000:
        food = spawn_food()

    pygame.draw.rect(screen, RED, (food["x"], food["y"], snake_block, snake_block))

    if snake_x == food["x"] and snake_y == food["y"]:
        length += food["weight"]
        score += food["weight"]
        food = spawn_food()

    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()