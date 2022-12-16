import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, RUNNING_SHIELD, RUNNING_HAMMER, JUMPING, JUMPING_SHIELD,\
    JUMPING_HAMMER, DUCKING, DUCKING_SHIELD, DUCKING_HAMMER, DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE

RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5
Y_POS_DUCK = 340


class Dinosaur(Sprite):
    def __init__(self):
        self.image_type = DEFAULT_TYPE
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 0
        self.dino_rect.y = 0
        self.step_index = 0
        self.running: bool = False
        self.jump: bool = False
        self.jump_vel = JUMP_VEL
        self.dino_duck = False
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.hammer = False
        self.show_text = False
        self.shield_time_up = 0
        self.hammer_time_up = 0
        self.show_text = False


    def update(self, user_input):
        if self.running:
            self.run()
        elif self.jump:
            self.dino_jump()
        elif self.dino_duck:
            self.duck()
        if user_input[pygame.K_UP] and not self.jump:
            self.running = False
            self.dino_duck = False
            self.jump = True
        elif user_input[pygame.K_DOWN] and not self.jump:
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
            self.image = RUN_IMG[self.image_type][0]
        else:
            self.image = RUN_IMG[self.image_type][1]

        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS

        self.step_index += 1

    def dino_jump(self):
        self.image = JUMP_IMG[self.image_type]
        self.dino_rect.y -= self.jump_vel * 4
        self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.jump = False
            self.jump_vel = JUMP_VEL
            # self.dino_rect.y += self.jump_vel * 4
            # self.jump_vel += 1

    def duck(self):
        self.image = DUCK_IMG[self.image_type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        self.step_index += 1
        self.dino_duck = False
        # O operador // divide e o resultado é sempre um numero inteiro, o mais proximo da divisão
        # O operador / divide e o resultado é um numero com ponto flutuante, o mais preciso
        # for i in range(0, 10):
        #    print(i // 5)

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
