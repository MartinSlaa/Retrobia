from random import choice
from brick import Brick

brick_L = 7
brick_H = 5

RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
MAGENTA = (255, 0, 255)

COLORS = [RED, ORANGE, YELLOW, GREEN, MAGENTA]

LEVEL_DESIGN = {1: ['1111111', '1111111', '1111111', '0000000', '0000000'],
                3: ['1111111', '1000001', '1011101', '1000001', '1111111']}

MAKE_RANDOM_LEVELS = True  # unless there is a definition in LEVEL_DESIGN, makes a random pattern


def make_random_level():
    """
    returns a list of brick_H strings each of them brick_L elements long (5,7) -> ['0101010', ..., '1111111']
        to be interpreted by build_bricks()
            0 - no block
            1 - block
    """
    return [''.join([choice('01') for j in range(brick_L)]) for i in range(brick_H)]


def build_bricks(all_bricks, level=1):
    # refresh brick structure
    all_bricks.empty()

    # defines the brick structure
    if level in LEVEL_DESIGN:
        level_des = LEVEL_DESIGN[level]
    else:
        level_des = make_random_level() if MAKE_RANDOM_LEVELS else LEVEL_DESIGN[1]

    # generate the bricks
    for j in range(brick_H):
        for i in range(brick_L):
            if level_des[j][i] == '1':
                brick = Brick(COLORS[j], 80, 30)
                brick.rect.x = 60 + 100 * i
                brick.rect.y = 60 + 40 * j
                all_bricks.add(brick)


if __name__ == '__main__':
    print(make_random_level())
