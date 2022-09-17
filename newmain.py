import pygame
import Player2
import Background2

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("screen")

def main():
    bg2 = Background2.Background2(screen)
    pl2 = Player2.Player2(screen)
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