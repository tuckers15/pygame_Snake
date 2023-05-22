import pygame
import random
import sys
import os
print(pygame.version.ver)

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

playerLength = 50
player = pygame.Rect(300, 250, playerLength, 50)
movement = None
apple = False
app = None
score = 0
scoreIncrement = 1


def detectBorderCollision(x, y):
    #take x y coordinates
    if x < 0 or x > 1280 or y < 0 or y > 720:
        return True
    return False


def detectAppleCollision(playX, playY, appX, appY):
    if abs(playX - appX) <= 50 and abs(playY - appY) <= 50:
        return True
    return False
       

run = True
while run:
    # Set up the font object
    font = pygame.font.Font(None, 36)

    #set fps
    clock.tick(60)

    #background
    screen.fill("purple")

    pygame.draw.rect(screen, (250, 0, 0), player)

    # Draw the score to the screen
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

    #player movement input
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        movement = "left"
    elif key[pygame.K_d] == True:
        movement = "right"
    elif key[pygame.K_w] == True:
        movement = "up"
    elif key[pygame.K_s] == True:
        movement = "down"

    #moves player
    if movement == "left":
        player.move_ip(-5, 0)
    elif movement == "right":
        player.move_ip(5, 0)
    elif movement == "up":
        player.move_ip(0, -5)
    elif movement == "down":
        player.move_ip(0, 5)

    
    if detectBorderCollision(player.x, player.y) == True:
        run = False
    
    if not apple:
        appleX = random.randrange(1200)
        appleY = random.randrange(700)
        app = pygame.Rect(appleX, appleY, 50, 50)
        apple = True

    pygame.draw.rect(screen, (0, 250, 250), app)

    if detectAppleCollision(player.x, player.y, app.x, app.y):
        score += scoreIncrement
        apple = False

    #update display
    pygame.display.update()

pygame.quit()       
