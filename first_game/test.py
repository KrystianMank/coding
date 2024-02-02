import pygame
from sys import exit

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

#inicjalizacja okna
pygame.init()

#ustawienie rozmiarów okna głównego i jego tytułu
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')

#utworzenie zegara
clock = pygame.time.Clock()

start_time = 0

#utworzenie fontu
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#utworzenie powierzchni
sky_surface = pygame.image.load('images/Sky.png').convert()
ground_surface = pygame.image.load('images/ground.png').convert()

snail_surface = pygame.image.load('images/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('images/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

#intro screen
player_stand = pygame.image.load('images/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400,200))

title_surface = test_font.render('My game', False, (64,64,64))
title_rect = title_surface.get_rect(center=(400, 50))

instruct_text = test_font.render('Press SPACE to continue',False,(64,64,64))
instruct_rect = instruct_text.get_rect(center=(400, 350))

game_active = False

score = 0

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
        score = 0
        
        snail_rect.left -= 10
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
            score = display_score()
    else:
        screen.fill((64,129,162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(title_surface, title_rect)

        score_text = test_font.render(f'Final score: {score}', False, (64, 64, 64))
        score_rect = score_text.get_rect(center=(400, 350))

        if score == 0:
            screen.blit(instruct_text, instruct_rect)
        else:
            screen.blit(score_text, score_rect)

    #aktualizacja okna
    pygame.display.update()
    clock.tick(60)
    