import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

head_surf = pygame.Surface((25, 25))
head_surf.fill((0, 0, 255))

head_rect = head_surf.get_rect(center=(300, 300))

w_pressed = False
s_pressed = False
a_pressed = False
d_pressed = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            screen.fill((0, 0, 0))
            match(event.key):
                case pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                case pygame.K_w:
                    w_pressed = True
                    s_pressed = False
                    a_pressed =False
                    d_pressed = False
                case pygame.K_s:
                    w_pressed = False
                    s_pressed = True
                    a_pressed = False
                    d_pressed = False
                case pygame.K_a:
                    w_pressed = False
                    s_pressed = False
                    a_pressed = True
                    d_pressed = False
                case pygame.K_d:
                    pass
                    w_pressed = False
                    s_pressed = False
                    a_pressed = False
                    d_pressed = True

    if w_pressed:
        screen.fill((0, 0, 0))
        head_rect.y -= 25
        if head_rect.top <= 0:
            head_rect.top = 0

    if s_pressed:
        screen.fill((0, 0, 0))
        head_rect.y += 25
        if head_rect.bottom >= 600:
            head_rect.bottom = 600

    if a_pressed:
        screen.fill((0, 0, 0))
        head_rect.x -= 25
        if head_rect.left <= 0:
            head_rect.left = 0

    if d_pressed:
        screen.fill((0, 0, 0))
        head_rect.x += 25
        if head_rect.right>= 600:
            head_rect.right = 600

    screen.blit(head_surf, head_rect)

    pygame.display.update()
    clock.tick(60)
