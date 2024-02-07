import pygame
from sys import exit
from random import randint


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(300, 300))
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
        if self.direction == 'up':
            self.rect.y -= 25
            if self.rect.top <= 0:
                self.rect.top = 0
        elif self.direction == 'down':
            self.rect.y += 25
            if self.rect.bottom >= 600:
                self.rect.bottom = 600
        elif self.direction == 'left':
            self.rect.x -= 25
            if self.rect.left <= 0:
                self.rect.left = 0
        elif self.direction == 'right':
            self.rect.x += 25
            if self.rect.right >= 600:
                self.rect.right = 600

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

        rand = randint(1, 24)
        self.x_pos = rand * 25
        '''Poprawne umieszczanie klocka w wierszach i kolumnach'''
        rand = randint(1, 24)
        self.y_pos = rand * 25

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake = pygame.sprite.GroupSingle()
snake.add(Snake())

apple = pygame.sprite.GroupSingle()
apple.add(Apple())


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

    screen.fill((0, 0, 0))  # Clear the scree
    snake.draw(screen)  # Draw the snake
    snake.update(None, False)

    apple.draw(screen)
    apple.update()

    pygame.display.update()
    clock.tick(15)
