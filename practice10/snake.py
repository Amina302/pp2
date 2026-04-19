import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

white = (255, 255, 255)
green = (0, 200, 0)
red = (220, 0, 0)
black = (0, 0, 0)

font = pygame.font.SysFont(None, 35)
clock = pygame.time.Clock()


def draw_text(text, x, y):
    img = font.render(text, True, white)
    screen.blit(img, (x, y))


def random_food(snake):
    while True:
        x = random.randrange(0, WIDTH, BLOCK)
        y = random.randrange(0, HEIGHT, BLOCK)
        if [x, y] not in snake:
            return x, y


def game():
    x = WIDTH // 2
    y = HEIGHT // 2

    dx = 0
    dy = 0

    snake = []
    length = 1

    score = 0
    level = 1
    speed = 3

    food_x, food_y = random_food(snake)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -BLOCK
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = BLOCK
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -BLOCK
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = BLOCK
                    dx = 0

        x += dx
        y += dy

    
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            running = False

        screen.fill(black)

        pygame.draw.rect(screen, red, (food_x, food_y, BLOCK, BLOCK))

        head = [x, y]
        snake.append(head)

        if len(snake) > length:
            del snake[0]

        for part in snake[:-1]:
            if part == head:
                running = False

        for part in snake:
            pygame.draw.rect(screen, green, (part[0], part[1], BLOCK, BLOCK))

        if x == food_x and y == food_y:
            length += 1
            score += 1
            food_x, food_y = random_food(snake)

            if score % 3 == 0:
                level += 1
                speed += 2

        draw_text("Score: " + str(score), 10, 10)
        draw_text("Level: " + str(level), 470, 10)

        pygame.display.update()
        clock.tick(speed)

    pygame.quit()


game()