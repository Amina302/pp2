import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Practice 11")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
YELLOW = (255, 215, 0)
GREEN = (0, 200, 0)

player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 7

enemy_x = random.randint(100, 500)
enemy_y = -100
enemy_speed = 5

coins = []
score = 0

def spawn_coin():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(-600, -50)
    weight = random.choice([1, 2, 5]) 
    coins.append([x, y, weight])

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed

    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, WIDTH - 50)


    if score >= 10:
        enemy_speed = 7
    if score >= 20:
        enemy_speed = 10

    if random.randint(1, 50) == 1:
        spawn_coin()

    for coin in coins[:]:
        coin[1] += 5  

        if abs(player_x - coin[0]) < 30 and abs(player_y - coin[1]) < 30:
            score += coin[2]
            coins.remove(coin)
            continue

        if coin[1] > HEIGHT:
            coins.remove(coin)

    if abs(player_x - enemy_x) < 40 and abs(player_y - enemy_y) < 40:
        print("Game Over! Score:", score)
        running = False

    pygame.draw.rect(screen, GREEN, (player_x, player_y, 40, 60))

    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, 40, 60))

    for coin in coins:
        if coin[2] == 1:
            color = WHITE
        elif coin[2] == 2:
            color = YELLOW
        else:
            color = (255, 0, 255)

        pygame.draw.circle(screen, color, (coin[0], coin[1]), 10)

    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()