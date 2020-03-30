from constants import *
import pygame
import block
import hurdel
#git test


clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

block = block.Block()
hurdel = hurdel.Hurdel()

def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background
    block.draw(surface)
    hurdel.draw(surface)
    pygame.display.flip()



def update():
    block.update()
    hurdel.update()



if __name__ == "__main__":
    main()
