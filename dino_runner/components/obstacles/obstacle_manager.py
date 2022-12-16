import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus


class Obstacle_Manager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):

        obstacle_type = [
            Cactus(),
            Bird(),
        ]

        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0, 1)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    game.playing = False
                    game.death_count += 1
                self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
