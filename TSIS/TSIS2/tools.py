import pygame
from collections import deque

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BRUSH_SIZES = {
    1: 2,
    2: 5,
    3: 10
}

def flood_fill(surface, start_pos, fill_color):
    width, height = surface.get_size()
    target_color = surface.get_at(start_pos)

    if target_color == fill_color:
        return

    queue = deque([start_pos])
    visited = set()

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        current_color = surface.get_at((x, y))
        if current_color != target_color:
            continue

        surface.set_at((x, y), fill_color)

        queue.extend([
            (x+1, y), (x-1, y),
            (x, y+1), (x, y-1)
        ])