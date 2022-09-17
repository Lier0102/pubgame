import pygame

class Background2:
    def __init__(self, screen):
        self.screen = screen
        self.back_img = pygame.image.load("game_background.png") # load the background image
        self.back_img2 = pygame.image.load("game_background.png") # 2

        self.x1 = 0
        self.y1 = 0

        self.x2 = 1920
        self.y2 = 0

    def draw(self):
        self.screen.blit(self.back_img, (self.x1, self.y1))
        self.screen.blit(self.back_img2, (self.x2, self.y2))
    
    def update(self):
        self.x1 -= 1
        self.x2 -= 1

        if self.x2 <= -1920: # 화면에 끝에 닿으면
            self.x2 = 1920
        if self.x1 <= -1920: # 화면에 끝에 닿으면
            self.x1 = 1920
