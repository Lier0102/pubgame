import pygame # load pygame module
import Background
import Player

pygame.init() # init pygame

screen = pygame.display.set_mode((640, 960)) # set window resolution to 640, 960
pygame.display.set_caption("Juwon Game") # set the caption "Juwon Game"

def main():
    bg = Background.Background(screen)
    pl = Player.Player(screen)
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # if q key pressed(Q)uit
                if event.key == pygame.K_q:
                    pygame.quit()
                if event.key == pygame.K_RIGHT:
                    # 오른쪽 키가 눌렸다고 알려주기
                    pl.right = True
                if event.key == pygame.K_LEFT:
                    pl.left = True
                if event.key == pygame.K_UP:
                    pl.up = True
                if event.key == pygame.K_DOWN:
                    pl.down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    pl.right = False
                if event.key == pygame.K_LEFT:
                    pl.left = False
                if event.key == pygame.K_UP:
                    pl.up = False
                if event.key == pygame.K_DOWN:
                    pl.down = False
            
                    
        bg.draw() # draw the background image onto the screen
        pl.draw()
        bg.update() # scroll
        pl.update()
        pygame.display.update()

main() # start the game