import random
import pygame

from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.hammer import Hammer


class Power_Up_Manager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power(self, score):

        power_type = [
            Shield(),
            Hammer(),
        ]

        if len(self.power_ups) == 0 and self.when_appears == score:
            self.power_ups.append(power_type[random.randint(0, 1)])

    def update(self, score, game_speed, player):
        self.generate_power(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.image_type = power_up.power_type
                player.has_power_up = True
                player.shield = True
                player.hammer = True
                player.shield_time_up = power_up.start_time + (power_up.duration * 100)
                player.hammer_time_up = power_up.start_time + (power_up.duration * 100)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_powerups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
