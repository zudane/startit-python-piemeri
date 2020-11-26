import pygame

# Piemērs no lieliska resursa par spēles veidošanu ar pygame
# https://www.patternsgameprog.com/series/discover-python-and-patterns/

pygame.init()
pygame.display.set_caption("StartIT kursu spēle")
window = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
FPS = 30
playtime = 0.0
x = 120
y = 120

while True:
    milliseconds = clock.tick(FPS) 
    playtime += milliseconds / 1000.0 

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = False
            break
        elif event.key == pygame.K_RIGHT:
            x += 8
        elif event.key == pygame.K_LEFT:
            x -= 8
        elif event.key == pygame.K_DOWN:
            y += 8
        elif event.key == pygame.K_UP:
            y -= 8
    
    text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
    pygame.display.set_caption(text)
    window.fill((0,0,0))
    pygame.draw.rect(window,(0,0,255),(x,y,100,100))
    pygame.display.update() 
    
pygame.quit()