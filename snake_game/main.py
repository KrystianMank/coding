import pygame
from sys import exit
from random import randint


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=(300, 300))
        self.direction = None
        self.head_x = self.rect.centerx
        self.head_y = self.rect.centery

    def player_input(self, key_pressed):
        if key_pressed == pygame.K_w and self.direction != 'down':
            self.direction = 'up'
        elif key_pressed == pygame.K_s and self.direction != 'up':
            self.direction = 'down'
        elif key_pressed == pygame.K_a and self.direction != 'right':
            self.direction = 'left'
        elif key_pressed == pygame.K_d and self.direction != 'left':
            self.direction = 'right'

    def move(self):
        global game_active
        if self.direction == 'up':
            self.rect.y -= 25
            if self.rect.top <= -25:
                self.rect.topleft = (300, 300)
                game_active = False

        elif self.direction == 'down':
            self.rect.y += 25
            if self.rect.bottom >= 625:
                self.rect.topleft = (300, 300)
                game_active = False

        elif self.direction == 'left':
            self.rect.x -= 25
            if self.rect.left <= -25:
                self.rect.topleft = (300, 300)
                game_active = False

        elif self.direction == 'right':
            self.rect.x += 25
            if self.rect.right >= 625:
                self.rect.topleft = (300, 300)
                game_active = False

    def get_pos(self):
        return self.head_x, self.head_y

    def update(self, key_pressed, update):
        global head_pos
        if update:
            self.player_input(key_pressed)
        else:
            self.move()
            self.head_x = self.rect.centerx
            self.head_y = self.rect.centery
        head_pos = (self.head_x, self.head_y)
        head_pos_array.append(head_pos)
        


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill((255, 0, 0))

        rand1 = randint(1, 23)
        self.x_pos = rand1 * 25

        rand2 = randint(1, 23)
        self.y_pos = rand2 * 25

        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))


class SnakeBody(Snake):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill((0, 255, 0))
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))


def collision():
    global score, head_pos_array, game_active
    score_text = text_font.render(f'Your score: {score}', False, (55, 55, 55), None)
    score_text_rect = score_text.get_rect(midleft=(25, 650))
    screen.blit(score_text, score_text_rect)

    if pygame.sprite.spritecollide(snake_head.sprite, apple, True):
        apple.add(Apple())
        snake_body.add(SnakeBody(head_pos_array[0]))
        score += 1
    else:
        head_pos_array.clear()

    if pygame.sprite.spritecollide(apple.sprite, snake_body, True):
        apple.add(Apple())




pygame.init()
screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption('Snake')

# Font
text_font = pygame.font.Font(None, 25)

# Score display
score_display_surf = pygame.Surface((600, 100))
score_display_surf.fill('#ffffff')
score_display = score_display_surf.get_rect(topleft=(0, 600))

# GameOver/Intro screen
over = text_font.render('Game Over... Press any key to continue', False, 'White')
over_rect = over.get_rect(center=(300, 300))

# Game clock
clock = pygame.time.Clock()

# Sprites
snake_head = pygame.sprite.GroupSingle()
snake_head.add(Snake())

apple = pygame.sprite.GroupSingle()
apple.add(Apple())

snake_body = pygame.sprite.Group()

# Global variables
score = 0

game_active = False

head_pos = (None, None)

head_pos_array = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            snake_head.update(event.key, True)
            game_active = True

    screen.fill((0, 0, 0))  # Clear the screen

    screen.blit(score_display_surf, score_display)

    if game_active:
        snake_head.draw(screen)  # Draw the snake
        snake_head.update(None, False)

        apple.draw(screen)  # Draw the apple
        apple.update()

        snake_body.draw(screen)
        snake_body.update(None, False)


        collision()

    else:
        screen.blit(over, over_rect)
        collision()
        score = 0
        snake_body.empty()

    pygame.display.update()
    clock.tick(15)
