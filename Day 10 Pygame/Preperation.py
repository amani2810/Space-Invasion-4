STEPS:
1) go to pypi.org
2) install pygame : https://pypi.org/project/pygame/
get the pip install code: pip install pygame
open terminal in Pycharm and install the package
3) Now we can start coding in pycharm IDE
Tip: glance over the pygame docs: https://www.pygame.org/docs/


# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()