import pygame # load pygame module

pygame.init() # init pygame

screen = pygame.display.set_mode((640, 960)) # set window resolution to 640, 960
pygame.display.set_caption("Juwon Game") # set the caption "Juwon Game"

class Background:
    def __init__(self, screen): # initializer
        self.screen = screen # initialize screen object
        self.back_img = pygame.image.load("background.png") # load the background image
        self.back_img2 = pygame.image.load("background.png") # 2

        self.x1 = 0
        self.y1 = 0

        self.x2 = 0
        self.y2 = -960

    def draw(self): # draw the background image onto the screen
        self.screen.blit(self.back_img, (self.x1,self.y1)) # scroll the background image onto the screen
        self.screen.blit(self.back_img2, (self.x2,self.y2))
    
    def update(self):
        self.y1 += 1
        self.y2 += 1 # 동시에 화면 밑으로 내려 주다가

        if self.y2 >= 960: # 화면에 끝에 닿으면
            self.y2 = -960
        if self.y1 >= 960:
            self.y1 = -960

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.player_img = pygame.image.load('player2.png')
        self.x1 = 320
        self.y1 = 700
    
    def draw(self):
        self.screen.blit(self.player_img, (self.x1,self.y1))
        

def main():
    bg = Background(screen)
    while True: # main game loop
        bg.draw() # draw the background image onto the screen
        bg.update() # scroll
        pygame.display.update()

main() # start the game