import pygame
import random
from racer import Player, Enemy, PowerUp
from ui import main_menu, game_over
from persistence import load_settings, save_settings, load_leaderboard, save_score

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

settings = load_settings()

player = Player()
enemies = []
powerups = []

state = "menu"

score = 0
distance = 0

enemy_speed = 5


def spawn_enemy():
    enemies.append(Enemy(enemy_speed))


def spawn_powerup():
    powerups.append(PowerUp(random.choice(["nitro", "shield", "repair"])))


running = True
spawn_timer = 0

while running:
    screen.fill((30,30,30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state = "game"
                if event.key == pygame.K_l:
                    state = "leaderboard"
                if event.key == pygame.K_s:
                    state = "settings"

        elif state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                if event.key == pygame.K_RIGHT:
                    player.move_right()

    if state == "menu":
        main_menu(screen)

    elif state == "game":
        spawn_timer += 1
        distance += 1

        if spawn_timer % 60 == 0:
            spawn_enemy()

        if spawn_timer % 200 == 0:
            spawn_powerup()

        for e in enemies:
            e.update()
            pygame.draw.rect(screen, (255,0,0), (e.x, e.y, 40, 80))

            if abs(e.y - player.y) < 50 and e.lane == player.lane:
                if player.shield:
                    player.shield = False
                else:
                    state = "game_over"
                    save_score("Player", score, distance)

        for p in powerups:
            p.y += 4
            pygame.draw.rect(screen, (0,255,0), (p.x, p.y, 30, 30))

            if abs(p.y - player.y) < 50 and p.lane == player.lane:
                if p.type == "shield":
                    player.shield = True
                elif p.type == "nitro":
                    player.nitro = 120
                elif p.type == "repair":
                    score += 50

        if player.nitro > 0:
            enemy_speed = 8
            player.nitro -= 1
        else:
            enemy_speed = 5

        pygame.draw.rect(screen, (0,0,255), (player.x, player.y, 40, 80))

        score += 1


    elif state == "game_over":
        game_over(screen, score, distance)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            player = Player()
            enemies = []
            powerups = []
            score = 0
            distance = 0
            state = "game"

        if keys[pygame.K_m]:
            state = "menu"

    pygame.display.update()
    clock.tick(60)

pygame.quit()