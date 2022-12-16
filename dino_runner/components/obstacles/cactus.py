import random

from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from dino_runner.components.obstacles.obstacle import Obstacle

CACTUS = [
    (SMALL_CACTUS, 325),
    (LARGE_CACTUS, 300),
]


class Cactus(Obstacle):

    def __init__(self):
        image, cactus_y_pos = CACTUS[random.randint(0, 1)]
        index = random.randint(0, 2)
        super().__init__(image[index])
        self.rect.y = cactus_y_pos
