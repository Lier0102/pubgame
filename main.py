import pygame # load pygame module

pygame.init() # init pygame

screen = pygame.display.set_mode((640, 960)) # set window resolution to 640, 960
pygame.display.set_caption("Juwon Game") # set the caption "Juwon Game"

class Background:
    def __init__(self, screen): # initializer
        self.screen = screen # initialize screen object
        self.back_img = pygame.image.load("background.png") # load the background image
    
    def draw(self): # draw the background image onto the screen
        self.screen.blit(self.back_img, (0,0))

def main():
    bg = Background(screen)
    while True: # main game loop
        bg.draw() # draw the background image onto the screen
        pygame.display.update()

main() # start the game