import pygame

def draw_text(screen, text, x, y, size=30):
    font = pygame.font.SysFont("Arial", size)
    render = font.render(text, True, (255,255,255))
    screen.blit(render, (x, y))


def main_menu(screen):
    screen.fill((0,0,0))
    draw_text(screen, "RACER GAME", 100, 100, 40)
    draw_text(screen, "Press ENTER to Play", 80, 250)
    draw_text(screen, "Press L - Leaderboard", 80, 300)
    draw_text(screen, "Press S - Settings", 80, 350)


def game_over(screen, score, distance):
    screen.fill((0,0,0))
    draw_text(screen, "GAME OVER", 120, 150, 40)
    draw_text(screen, f"Score: {score}", 120, 220)
    draw_text(screen, f"Distance: {distance}", 120, 260)
    draw_text(screen, "R - Retry | M - Menu", 80, 320)