#!/usr/bin/python

import pygame, sys,time
from pygame.locals import *

from launcher import *
import rock
from colors import *
import target

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500,400),0,32) #makes window
ground      = pygame.Rect(0,380,500,20) #ground obj
myLauncher  = Launcher(0,380)
myRock      = rock.Rock(0,380)
myTarget    = target.Target()
FPS = 30
fpsClock=pygame.time.Clock()


def draw_world(surf): #draws everything for scenery
    surf.fill(SKY_COLOR) #fills sky background
    pygame.draw.rect(surf,GRASS_GREEN,ground)
    fontObj = pygame.font.Font('freesansbold.ttf', 32)  #font obj
    textSurfaceObj = fontObj.render('Launchr 1.0', True, BLACK, SKY_COLOR) #text obj
    textRectObj = textSurfaceObj.get_rect() #text box
    textRectObj.center = (250, 25) #text box center
    surf.blit(textSurfaceObj, textRectObj) #puts text to screen


def displayText(str,surf,size,x,y,color): #string, surface, font size, center, color
    fontObj1 = pygame.font.Font('freesansbold.ttf', size)  #font obj
    textSurfaceObj1 = fontObj1.render(str, True, color, SKY_COLOR) #text obj
    textRectObj1 = textSurfaceObj1.get_rect() #text box
    textRectObj1.center = (x, y) #text box center
    surf.blit(textSurfaceObj1,textRectObj1)
    pygame.display.update()
    time.sleep(1)
       
def main(): #main loop
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    delta=-3
                    myLauncher.changeAngle(delta)
                elif event.key==pygame.K_UP:
                    delta=3
                    myLauncher.changeAngle(delta)
                elif event.key==pygame.K_LEFT:
                    delta=-2
                    myLauncher.changeMagnitude(delta)
                elif event.key==pygame.K_RIGHT:
                    delta=2
                    myLauncher.changeMagnitude(delta)
                elif event.key==pygame.K_SPACE and not myRock.isMoving():
                    myLauncher.fire(myRock)
                    print "fire!"
            if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

        
        
        #game logic
        myRock.move(1.0/FPS)
        if(myRock.y>380 and myTarget.hitBy(myRock)==False):
           myRock.moveTo(0,380)
           displayText("ya missed, m8",DISPLAYSURF,16,250,250,RED)
           
        if(myTarget.hitBy(myRock)):
           myRock.moveTo(0,380)
           displayText("ya did it, m8",DISPLAYSURF,16,250,250,RED)

        draw_world(DISPLAYSURF)   
        myLauncher.draw(DISPLAYSURF)
        myRock.draw(DISPLAYSURF)
        myTarget.draw(DISPLAYSURF)
        pygame.display.update()
        fpsClock.tick(FPS)


main()
