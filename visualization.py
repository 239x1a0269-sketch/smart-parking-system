import pygame

pygame.init()

WIDTH = 800
HEIGHT = 500

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Parking Visualization"
)

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_slots(occupied):

    screen.fill(WHITE)

    for i in range(20):

        x = 50 + (i % 10) * 70
        y = 100 + (i // 10) * 120

        color = GREEN

        if i + 1 in occupied:

            color = RED

        pygame.draw.rect(
            screen,
            color,
            (x, y, 50, 80)
        )

    pygame.display.update()