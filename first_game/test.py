import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load('images/player/player_walk_1.png').convert_alpha()
        player_walk2 = pygame.image.load('images/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk1, player_walk2]
        self.player_index = 0
        self.player_jump = pygame.image.load('images/player/jump.png').convert_alpha()
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.5)

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity -= 20
            self.jump_sound.play()
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            self.gravity = 0

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]


    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_1 = pygame.image.load('images/fly/Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('images/fly/Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load('images/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('images/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900,1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.2
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 10
        self.destroy()

    def destroy(self):
        if self.rect.x < -100:
            self.kill()

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 10

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        #grafika skoku gdy nie jest na ziemii
        player_surf = player_jump
    else:
        #animacja chodzenia gdy jest na ziemii
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]

#inicjalizacja okna
pygame.init()

#ustawienie rozmiarów okna głównego i jego tytułu
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')

#utworzenie zegara
clock = pygame.time.Clock()

start_time = 0

#muzyka
bgMusic = pygame.mixer.Sound('audio/music.wav')
bgMusic.set_volume(0.5)
bgMusic.play(loops=-1)

#utworzenie fontu
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#utworzenie powierzchni
sky_surface = pygame.image.load('images/Sky.png').convert()
ground_surface = pygame.image.load('images/ground.png').convert()

#utworzenie player sprite
player = pygame.sprite.GroupSingle()
player.add(Player())

#obstacle group
obstacle_group = pygame.sprite.Group()

#Snail
snail_frame1 = pygame.image.load('images/snail/snail1.png').convert_alpha()
snail_frame2 = pygame.image.load('images/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame1, snail_frame2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

#Fly
fly_frame1 = pygame.image.load('images/fly/fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('images/fly/fly2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []

#Player
player_walk1 = pygame.image.load('images/player/player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load('images/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk1, player_walk2]
player_index = 0
player_jump = pygame.image.load('images/player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
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

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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
                    start_time = pygame.time.get_ticks()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail'])))
                # if randint(0,2):
                #     obstacle_rect_list.append(snail_surf.get_rect(midbottom=(randint(900, 1100), 300)))
                # else:
                #     obstacle_rect_list.append(fly_surf.get_rect(midbottom=(randint(900, 1100), 210)))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

    if game_active:        
        #umieszczenie powierzchni na okno główne
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        display_score()
        score = int((pygame.time.get_ticks()-start_time)/1000)

        #Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #Player
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300
        #     player_gravity = 0
        # player_animation()
        # screen.blit(player_surf,player_rect)

        #Metody sprite'ów
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        #collision
        game_active = collision_sprite()
        # game_active = collisions(player_rect, obstacle_rect_list)
    else:
        screen.fill((64, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(title_surface, title_rect)
        obstacle_rect_list.clear()

        score_text = test_font.render(f'Final score: {score}', False, (64, 64, 64))
        score_rect = score_text.get_rect(center=(400, 350))

        if score == 0:
            screen.blit(instruct_text, instruct_rect)
        else:
            screen.blit(score_text, score_rect)

    #aktualizacja okna
    pygame.display.update()
    clock.tick(60)
    