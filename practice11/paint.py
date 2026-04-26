import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Paint Practice 11")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)

screen.fill(WHITE)

mode = "brush"
drawing = False
last_pos = None


def draw_square(pos):
    x, y = pos
    pygame.draw.rect(screen, RED, (x, y, 60, 60), 2)

def draw_right_triangle(pos):
    x, y = pos
    pygame.draw.polygon(screen, GREEN, [
        (x, y),
        (x + 60, y),
        (x, y + 60)
    ], 2)

def draw_equilateral_triangle(pos):
    x, y = pos
    pygame.draw.polygon(screen, BLUE, [
        (x, y + 60),
        (x + 30, y),
        (x + 60, y + 60)
    ], 2)

def draw_rhombus(pos):
    x, y = pos
    pygame.draw.polygon(screen, YELLOW, [
        (x, y + 30),
        (x + 30, y),
        (x + 60, y + 30),
        (x + 30, y + 60)
    ], 2)

def draw_brush(start, end):
    pygame.draw.line(screen, BLACK, start, end, 5)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = "square"
            elif event.key == pygame.K_2:
                mode = "right_triangle"
            elif event.key == pygame.K_3:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_4:
                mode = "rhombus"
            elif event.key == pygame.K_c:
                screen.fill(WHITE)

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            pos = pygame.mouse.get_pos()

            if mode == "square":
                draw_square(pos)
            elif mode == "right_triangle":
                draw_right_triangle(pos)
            elif mode == "equilateral_triangle":
                draw_equilateral_triangle(pos)
            elif mode == "rhombus":
                draw_rhombus(pos)

            last_pos = pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None

        if event.type == pygame.MOUSEMOTION and drawing and mode == "brush":
            current_pos = pygame.mouse.get_pos()
            if last_pos:
                draw_brush(last_pos, current_pos)
            last_pos = current_pos

    pygame.display.update()
    clock.tick(60)

pygame.quit()