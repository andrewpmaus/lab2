import pygame
from colors import *

G = 10.0

class Rock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v_x = 0
        self.v_y = 0

    def move(self, time):
        self.x += self.v_x*time
	if self.y < 400:	
	    self.v_y += G*time
	    self.y -= self.v_y*time

    def isMoving(self):
        if self.v_x is not 0 or self.v_y is not 0:
            return True
        else:
            return False

    def draw(self, surf):
        #TODO, draw to surface
        r = pygame.Rect(0,0,10,10)
        r.center = (self.x, self.y)
        pygame.draw.rect(surf, ROCK_COLOR, r)
    
