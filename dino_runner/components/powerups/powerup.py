import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class PowerUp(Sprite):
    def __init__(self, image, power_type):
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 900)
        self.rect.y = random.randint(125, 175)
        self.power_type = power_type
        self.start_time = 0
        self.duration = random.randint(20, 30)

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed

        if self.rect.x < self.rect.width:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
