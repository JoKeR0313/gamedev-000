import sys
import pygame

pygame.init()

size = width, height = 840, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

b = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    curr_time = pygame.time.get_ticks()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    blur = screen.copy()
    blur.set_alpha(180)
    screen.fill(black)
    screen.blit(blur, blur.get_rect())
    screen.blit(ball, ballrect)
    pygame.display.flip()

    if 16 > pygame.time.get_ticks() - curr_time:
        time_to_wait = 16 - (pygame.time.get_ticks() - curr_time)
        pygame.time.delay(time_to_wait)
