import pygame
import random

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (220, 0, 0)
blue = (0, 100, 255)
yellow = (255, 215, 0)

font = pygame.font.SysFont(None, 35)

player_x = 170
player_y = 500
player_w = 60
player_h = 90
player_speed = 7

enemy_x = random.randint(50, 290)
enemy_y = -100
enemy_w = 60
enemy_h = 90
enemy_speed = 6

coin_x = random.randint(60, 320)
coin_y = -50
coin_size = 25
coin_speed = 5

coins = 0

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 40:
        player_x -= player_speed

    if keys[pygame.K_RIGHT] and player_x < 300:
        player_x += player_speed

    enemy_y += enemy_speed

    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, 290)

    coin_y += coin_speed

    if coin_y > HEIGHT:
        coin_y = -50
        coin_x = random.randint(60, 320)

    screen.fill((80, 80, 80))

    for y in range(0, HEIGHT, 60):
        pygame.draw.rect(screen, white, (195, y, 10, 30))

    pygame.draw.rect(screen, blue, (player_x, player_y, player_w, player_h))

    pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_w, enemy_h))

    pygame.draw.circle(screen, yellow, (coin_x, coin_y), coin_size)


    player_rect = pygame.Rect(player_x, player_y, player_w, player_h)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_w, enemy_h)
    coin_rect = pygame.Rect(coin_x - coin_size, coin_y - coin_size, coin_size * 2, coin_size * 2)

    if player_rect.colliderect(coin_rect):
        coins += 1
        coin_y = -50
        coin_x = random.randint(60, 320)


    if player_rect.colliderect(enemy_rect):
        running = False

    text = font.render("Coins: " + str(coins), True, white)
    screen.blit(text, (250, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()