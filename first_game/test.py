import pygame
from sys import exit

#inicjalizacja okna
pygame.init()

#ustawienie rozmiarów okna głównego i jego tytułu
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')

#utworzenie zegara
clock = pygame.time.Clock()

#utworzenie fontu
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#utworzenie powierzchni
sky_surface = pygame.image.load('images/Sky.png').convert()
ground_surface = pygame.image.load('images/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('images/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('images/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('col')
                
    #umieszczenie powierzchni na okno główne
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    
    snail_rect.left -= 4
    if snail_rect.left < -100:
      snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)
    
    screen.blit(player_surf,player_rect)
    
    # if player_rect.colliderect(snail_rect):
    #     print('colisonn')
        
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print('colision')
    
    #aktualizacja okna     
    pygame.display.update()
    clock.tick(60)
    