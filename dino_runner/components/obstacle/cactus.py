import random

from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.components.obstacle.obstacle import Obstacle

CACTUS = [
        (SMALL_CACTUS, 325)
        ]

class Cactus(Obstacle):
  
    def __init__(self):
        image, cactus_y_pos = CACTUS[0]
        index = random.randint(0, 2)
        super().__init__(image[index])
        self.rect.y = cactus_y_pos
    