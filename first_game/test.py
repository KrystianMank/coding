import pygame
from sys import exit

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)

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

# score_surface = test_font.render('My game', False, (64,64,64))
# score_rect = score_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load('images/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('images/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

player_gravity = 0

game_active = True

start_time = 0

while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity -= 20
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity -= 20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 600
                    start_time = pygame.time.get_ticks()
                
    if game_active:        
        #umieszczenie powierzchni na okno główne
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect,10)
        # screen.blit(score_surface,score_rect)
        display_score()
        
        snail_rect.left -= 4
        if snail_rect.left < -100:
            snail_rect.left = 800
        screen.blit(snail_surface,snail_rect)
        
        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
            player_gravity = 0
        screen.blit(player_surf,player_rect)
        
        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Yellow')
    #aktualizacja okna     
    pygame.display.update()
    clock.tick(60)
    