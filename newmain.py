import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("screen")

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

class Player2:
    def __init__(self, screen):
        self.screen = screen
        self.player_img = pygame.image.load('player.png')
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

def main():
    bg2 = Background2(screen)
    pl2 = Player2(screen)
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # if q key pressed(Q)uit
                if event.key == pygame.K_q:
                    pygame.quit()
                if event.key == pygame.K_RIGHT:
                    # 오른쪽 키가 눌렸다고 알려주기
                    pl2.right = True
                if event.key == pygame.K_LEFT:
                    pl2.left = True
                if event.key == pygame.K_UP:
                    pl2.up = True
                if event.key == pygame.K_DOWN:
                    pl2.down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    pl2.right = False
                if event.key == pygame.K_LEFT:
                    pl2.left = False
                if event.key == pygame.K_UP:
                    pl2.up = False
                if event.key == pygame.K_DOWN:
                    pl2.down = False

        bg2.draw() # draw the background image onto the screen
        pl2.draw()
        bg2.update() # scroll
        pl2.update()
        pygame.display.update()

main()