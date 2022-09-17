import pygame

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.player_img = pygame.image.load('player2.png')
        self.x1 = 280
        self.y1 = 700
        self.right = False
        self.left = False
        self.up = False
        self.down = False
    
    def draw(self):
        self.screen.blit(self.player_img, (self.x1,self.y1))

    def update(self):
        if self.right == True:
            self.x1 += 2
        if self.left == True:
            self.x1 -= 2
        if self.up == True:
            self.y1 -= 2
        if self.down == True:
            self.y1 += 2