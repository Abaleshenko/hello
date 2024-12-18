import random
from asciimatics.screen import Screen
import time

def moving_dots(screen):
    dots = [(random.randint(0, screen.width - 1), random.randint(0, screen.height - 1)) for _ in range(20)]
    for _ in range(200):
        screen.clear()
        for x, y in dots:
            screen.print_at('*', x, y)
        dots = [(random.randint(0, screen.width - 1), random.randint(0, screen.height - 1)) for _ in dots]
        screen.refresh()
        screen.sleep(0.1)

Screen.wrapper(moving_dots)
