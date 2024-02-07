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

    def player_input(self, key_pressed):
        if key_pressed == pygame.K_w:
            self.direction = 'up'
        elif key_pressed == pygame.K_s:
            self.direction = 'down'
        elif key_pressed == pygame.K_a:
            self.direction = 'left'
        elif key_pressed == pygame.K_d:
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

    def update(self, key_pressed, update):
        if update:
            self.player_input(key_pressed)
        else:
            self.move()


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill((255, 0, 0))

        rand = randint(1, 23)
        self.x_pos = rand * 25

        rand = randint(1, 23)
        self.y_pos = rand * 25

        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))


def collision():
    global score
    score_text = text_font.render(f'Your score: {score}', False, (55, 55, 55), None)
    score_text_rect = score_text.get_rect(midleft=(25, 650))
    screen.blit(score_text, score_text_rect)

    if pygame.sprite.spritecollide(snake.sprite, apple, True):
        apple.add(Apple())
        score += 1


pygame.init()
screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption('Snake')

#Font
text_font = pygame.font.Font(None, 25)

#Score display
score_display_surf = pygame.Surface((600, 100))
score_display_surf.fill('#ffffff')
score_display = score_display_surf.get_rect(topleft=(0, 600))

#GameOver/Intro screen
over = text_font.render('Game Over... Press any key to continue', False, 'White')
over_rect = over.get_rect(center=(300, 300))

#Game clock
clock = pygame.time.Clock()

#Sprites
snake = pygame.sprite.GroupSingle()
snake.add(Snake())

apple = pygame.sprite.GroupSingle()
apple.add(Apple())

#Global variables
score = 0

game_active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            snake.update(event.key, True)
            game_active = True

    screen.fill((0, 0, 0))  # Clear the screen

    screen.blit(score_display_surf, score_display)

    if game_active:
        snake.draw(screen)  # Draw the snake
        snake.update(None, False)

        apple.draw(screen)  # Draw the apple
        apple.update()

        collision()
    else:
        score = 0
        screen.blit(over, over_rect)
        collision()

    pygame.display.update()
    clock.tick(15)
