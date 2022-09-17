import pygame

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
