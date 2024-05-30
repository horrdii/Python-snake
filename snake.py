import pygame
import random

# Define constants
BLOCK_SIZE = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GREEN = (0, 255, 0)

class Snake:
    def __init__(self):
        self.size = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.color = GREEN
        self.growing = False

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.get_head_position()
        x, y = cur
        if self.direction == pygame.K_UP:
            y -= BLOCK_SIZE
        elif self.direction == pygame.K_DOWN:
            y += BLOCK_SIZE
        elif self.direction == pygame.K_LEFT:
            x -= BLOCK_SIZE
        elif self.direction == pygame.K_RIGHT:
            x += BLOCK_SIZE

        # Screen wrapping logic
        x = x % SCREEN_WIDTH
        y = y % SCREEN_HEIGHT

        new_position = (x, y)
        if new_position in self.positions[2:]:
            self.reset()
        else:
            if self.growing:
                self.positions.insert(0, new_position)
                self.growing = False
            else:
                self.positions = [new_position] + self.positions[:-1]

    def grow(self):
        self.growing = True

    def reset(self):
        self.size = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.growing = False

    def change_direction(self, direction):
        if direction == pygame.K_UP and self.direction != pygame.K_DOWN:
            self.direction = direction
        elif direction == pygame.K_DOWN and self.direction != pygame.K_UP:
            self.direction = direction
        elif direction == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
            self.direction = direction
        elif direction == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
            self.direction = direction

    def draw(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, self.color, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
