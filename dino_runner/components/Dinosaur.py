import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

RUN_IMG = [RUNNING[0], RUNNING[1]]
X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5

DUCK_IMG = [DUCKING[0], DUCKING[1]]


class Dinosaur:
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 0
        self.dino_rect.y = 0
        self.step_index = 0
        self.running: bool = False
        self.jump: bool = False
        self.jump_vel = JUMP_VEL
        self.dino_duck: bool = False

    def update(self, user_input):

        if self.running:
            self.run()
        elif self.jump:
            self.dino_jump()

        if user_input[pygame.K_UP] and not self.jump:
            self.running = False
            self.dino_duck = False
            self.jump = True
        elif user_input[pygame.K_DOWN] and not self.dino_duck:
            self.running = False
            self.jump = False
            self.dino_duck = True
        elif not self.jump and not self.dino_duck:
            self.jump = False
            self.dino_duck = False
            self.running = True

        if self.step_index >= 9:
            self.step_index = 0

    def run(self):
        if self.step_index < 5:
            self.image = RUN_IMG[0]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = X_POS
            self.dino_rect.y = Y_POS
        else:
            self.image = RUN_IMG[1]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = X_POS
            self.dino_rect.y = Y_POS
            self.dino_duck = False

        self.step_index += 1

    def dino_jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_vel * 4
        self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y += self.jump_vel * 4
            self.jump_vel += 1
            self.dino_rect.y = Y_POS
            self.jump = False
            self.jump_vel = JUMP_VEL

    def dino_duck(self):
        self.image = DUCKING[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1
        self.dino_duck = False
        for i in range(0, 10):
            print(i // 5)

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
