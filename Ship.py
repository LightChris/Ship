import sys
import pygame
import math

from Classes.Vector import Vector

FPS = 40
NORMAL = 0
TURN_LEFT = 1
TURN_RIGHT = 2
SPEED_UP = 3
SPEED_DOWN = 4
STOP = 5


class Ship:
    def __init__(self, pos):
        # self.w = 45
        # self.h = 40
        self.rotate_speed = 5
        self.state = NORMAL
        self.pos = Vector(pos)
        self.image = pygame.Surface((45, 40), pygame.SRCALPHA)
        self.speed = Vector((0, 0))
        self.normal_speed = Vector((1, 0))  # Скорость и направление, сохраняемые при полном торможении
        self.max_speed = 10

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.state = SPEED_UP
            if event.key == pygame.K_DOWN:
                self.state = SPEED_DOWN
            if event.key == pygame.K_LEFT:
                self.state = TURN_LEFT
            if event.key == pygame.K_RIGHT:
                self.state = TURN_RIGHT
        if event.type == pygame.KEYUP:
            self.state = NORMAL

    def update(self):
        if self.state == TURN_LEFT:
            self.speed.rotate(-self.rotate_speed)
            pygame.transform.rotate(self.image, self.speed.angle)
        if self.state == TURN_RIGHT:
            self.speed.rotate(self.rotate_speed)
        if self.state == SPEED_UP:
            if self.speed.len() < self.max_speed:
                self.speed = self.speed + self.speed.normalize()
                if self.speed.len() == 0:
                    self.speed = self.normal_speed
        if self.speed.len() == 0:
            return
        if self.state == SPEED_DOWN:
            if self.speed.len() < 1:
                self.normal_speed = self.speed
                self.speed = Vector((0, 0))
            else:
                self.speed = self.speed - self.speed.normalize()
        self.pos += self.speed
        if self.pos.as_point()[0] > 800:
            self.pos = Vector((0, self.pos.as_point()[1]))
        if self.pos.as_point()[1] > 600:
            self.pos = Vector((self.pos.as_point()[0], 0))
        if self.pos.as_point()[1] < -1:
            self.pos = Vector((self.pos.as_point()[0], 599))
        if self.pos.as_point()[0] < -1:
            self.pos = Vector((799, self.pos.as_point()[1]))

    def draw(self):
        pygame.draw.lines(self.image, (155, 0, 0), False, [(40, 20), (38, 18), (32, 18), (32, 16), (26, 16),
                                                           (26, 18), (26, 15), (30, 10), (30, 8), (36, 8),
                                                           (36, 6), (30, 6), (28, 4), (20, 4), (14, 10), (10, 10),
                                                           (6, 14), (6, 24), (12, 30), (16, 30), (22, 36),
                                                           (30, 36),
                                                           (32, 34), (36, 34), (36, 32), (30, 32), (30, 30),
                                                           (26, 26), (26, 22), (26, 24), (32, 24), (32, 22),
                                                           (38, 22), (40, 20)])
        pygame.draw.rect(self.image, (255, 255, 255), self.image.get_rect(), 1)

    def render(self, screen):
        r = Vector(self.image.get_rect().center)
        rotate_image = pygame.transform.rotate(self.image, self.speed.angle)
        origin_rect = self.image.get_rect()
        rotate_rect = rotate_image.get_rect()
        rotate_rect.center = origin_rect.center
        rotate_rect.move_ip(self.pos.as_point())
        screen.blit(rotate_image, rotate_rect)
        pygame.draw.line(screen, (0, 255, 0), (self.pos + r).as_point(),
                         ((self.pos + self.speed * 5) + r).as_point())


pygame.init()
pygame.display.set_mode((800, 600))
screen = pygame.display.get_surface()

ship = Ship((400, 300))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        ship.events(event)
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(FPS)
    ship.update()
    ship.draw()
    screen.fill((0, 0, 0))
    ship.render(screen)
    pygame.display.flip()
