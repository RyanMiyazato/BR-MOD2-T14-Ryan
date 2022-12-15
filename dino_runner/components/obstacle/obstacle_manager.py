from dino_runner.components.obstacle.cactus import Cactus

class Obstacle_Manager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                self.obstacles.remove(obstacle)
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        


    