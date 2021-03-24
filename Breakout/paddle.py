import pygame

BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    # This class represents a paddle. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # pass in the color of the car and its x and y position, width and height.
        # set background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw paddle (rectangle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        self._w = width
        self._h = height

    @property
    def position(self):
        return self.rect.x, self.rect.y

    @property
    def width(self):
        return self._w

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # keep paddle on screen
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # keep paddle on screen
        if self.rect.x > 700:
            self.rect.x = 700