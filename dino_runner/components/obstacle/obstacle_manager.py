from dino_runner.components.obstacle.cactus import Cactus
from dino_runner.components.obstacle.bird import Bird

class Obstacle_Manager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):

       obstacle_type = [
           Cactus(),
           Bird(),

       ]
        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0,1)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                self.obstacles.remove(obstacle)
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        


    