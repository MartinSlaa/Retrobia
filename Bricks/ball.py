import pygame
from random import randint
BLACK = (0,0,0)
class Ball(pygame.sprite.Sprite):
    #Class for the ball, from the "Sprite" class in Pygame
    def __init__(self, color, width, height):
        #call the parent class (Sprite) constructor
        super().__init__()
        #pass in the color of the ball, its width and height.
        #Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        #Draw the ball (rectangle)
        pygame.draw.rect(self.image, color, [0,0, width, height])
        self.velocity = [randint(4,4),randint(-4,4)]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self._status = False

    @property
    def moving(self):
        return self._status

    def move(self):
        self._status = True

    def stop(self):
        self._status = False

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # ball moving only horizontally
        if self.velocity[1] == 0:
            self.velocity[1] += 1
        if self._status:
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]
            # ball moving only horizontally
            if self.velocity[1] == 0:
                self.velocity[1] += 1

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-4,4)
        if self._status:
            self.velocity[0] = -self.velocity[0]
            self.velocity[1] = randint(-4,4)

    def moveToPaddle(self, paddle):
        self.rect.x = paddle.position[0] + paddle.width//2
        self.rect.y = paddle.position[1]-10