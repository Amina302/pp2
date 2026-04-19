import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen.fill(white)

clock = pygame.time.Clock()

drawing = False
start_pos = None

tool = "brush"
color = black

font = pygame.font.SysFont(None, 28)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if tool == "rect":
                x = min(start_pos[0], end_pos[0])
                y = min(start_pos[1], end_pos[1])
                w = abs(start_pos[0] - end_pos[0])
                h = abs(start_pos[1] - end_pos[1])
                pygame.draw.rect(screen, color, (x, y, w, h), 2)

            if tool == "circle":
                radius = abs(end_pos[0] - start_pos[0]) // 2
                pygame.draw.circle(screen, color, start_pos, radius, 2)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                tool = "brush"
            if event.key == pygame.K_r:
                tool = "rect"
            if event.key == pygame.K_c:
                tool = "circle"
            if event.key == pygame.K_e:
                tool = "eraser"

            # Colors
            if event.key == pygame.K_1:
                color = black
            if event.key == pygame.K_2:
                color = red
            if event.key == pygame.K_3:
                color = green
            if event.key == pygame.K_4:
                color = blue

    if drawing:
        mouse = pygame.mouse.get_pos()

        if tool == "brush":
            pygame.draw.circle(screen, color, mouse, 5)

        if tool == "eraser":
            pygame.draw.circle(screen, white, mouse, 15)

    pygame.draw.rect(screen, white, (0, 0, WIDTH, 30))
    text = font.render("B-Brush R-Rect C-Circle E-Eraser | 1-Black 2-Red 3-Green 4-Blue", True, black)
    screen.blit(text, (10, 5))

    pygame.display.update()
    clock.tick(60)

pygame.quit()