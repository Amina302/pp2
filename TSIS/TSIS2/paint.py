import pygame
import sys
from datetime import datetime
from tools import flood_fill, BRUSH_SIZES

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 2 Paint")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

current_color = (0, 0, 0)
brush_size = 2

tool = "pencil"  
drawing = False
start_pos = None
last_pos = None

font = pygame.font.SysFont("Arial", 24)
text_input = ""
text_pos = None
typing = False

def draw_line(surface, start, end, color, size):
    pygame.draw.line(surface, color, start, end, size)

def draw_rect(surface, start, end, color, size):
    rect = pygame.Rect(start[0], start[1],
                       end[0] - start[0],
                       end[1] - start[1])
    pygame.draw.rect(surface, color, rect, size)

def draw_circle(surface, start, end, color, size):
    radius = int(((end[0]-start[0])**2 + (end[1]-start[1])**2) ** 0.5)
    pygame.draw.circle(surface, color, start, radius, size)

def save_canvas():
    time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"canvas_{time}.png"
    pygame.image.save(canvas, filename)
    print("Saved:", filename)

running = True

while running:
    screen.fill((200, 200, 200))
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                brush_size = BRUSH_SIZES[1]
            if event.key == pygame.K_2:
                brush_size = BRUSH_SIZES[2]
            if event.key == pygame.K_3:
                brush_size = BRUSH_SIZES[3]

            if event.key == pygame.K_p:
                tool = "pencil"
            if event.key == pygame.K_l:
                tool = "line"
            if event.key == pygame.K_r:
                tool = "rect"
            if event.key == pygame.K_c:
                tool = "circle"
            if event.key == pygame.K_f:
                tool = "fill"
            if event.key == pygame.K_t:
                tool = "text"
                typing = True
                text_input = ""
                text_pos = None

            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save_canvas()

            if typing:
                if event.key == pygame.K_RETURN:
                    if text_pos:
                        img = font.render(text_input, True, current_color)
                        canvas.blit(img, text_pos)
                    typing = False
                elif event.key == pygame.K_ESCAPE:
                    typing = False
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if tool == "fill":
                flood_fill(canvas, pos, current_color)

            elif tool == "text":
                text_pos = pos

            else:
                drawing = True
                start_pos = pos
                last_pos = pos

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = pygame.mouse.get_pos()

                if tool == "line":
                    draw_line(canvas, start_pos, end_pos, current_color, brush_size)

                elif tool == "rect":
                    draw_rect(canvas, start_pos, end_pos, current_color, brush_size)

                elif tool == "circle":
                    draw_circle(canvas, start_pos, end_pos, current_color, brush_size)

            drawing = False
            start_pos = None
            last_pos = None

        if event.type == pygame.MOUSEMOTION:
            if drawing and tool == "pencil":
                current_pos = pygame.mouse.get_pos()
                draw_line(canvas, last_pos, current_pos, current_color, brush_size)
                last_pos = current_pos

    if drawing and tool == "line":
        preview = canvas.copy()
        pygame.draw.line(preview, current_color, start_pos, pygame.mouse.get_pos(), brush_size)
        screen.blit(preview, (0, 0))

    else:
        screen.blit(canvas, (0, 0))

    if typing and text_pos:
        preview_text = font.render(text_input, True, current_color)
        screen.blit(preview_text, text_pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()