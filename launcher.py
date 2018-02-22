from numpy import cos, sin, pi
import pygame
from colors import *

MAX_MAG = 100
MIN_MAG = 10
MAX_ANGLE = 90
MIN_ANGLE = 0

class Launcher:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = 100
        self.angle = 45
        self.width=4
        # the launcher is located at (x,y)
        # with the initial state:
        # magnitude = 20
        # angle = 45 deg

    def changeMagnitude(self, delta):
        if abs(self.magnitude) <= MAX_MAG and abs(self.magnitude) >= MIN_MAG:
            self.magnitude += delta
            # adjust the magnitude
            # within MIN / MAX bounds

    def changeAngle(self, delta):
        if abs(self.angle) <= MAX_ANGLE and abs(self.angle) >= MIN_ANGLE:
            self.angle += delta
            # adjust the angle
            # within MIN / MAX bounds
    
    def draw(self, surf):
        dx = self.magnitude*cos(self.angle*pi/180)
        dy = self.magnitude*sin(self.angle*pi/180)
        pygame.draw.line(surf, BROWN, (self.x,self.y),(self.x+dx,self.y-dy),self.width)

    def fire(self, rock):
        rock.v_x = self.magnitude*cos(self.angle*pi/180)
        rock.v_y = -1*self.magnitude*sin(self.angle*pi/180)
        
