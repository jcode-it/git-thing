#####################################################################
# author:James Slayton
# date:3/23/26
# description: program2 
#####################################################################
import pygame
from random import randint, choice
from Item import *
from Constants import *


class Person(pygame.sprite.Sprite, Item):
    def __init__(self, name="player 1", x=0, y=0, size=1):
        Item.__init__(self,name,x,y,size)
        self.size = (size,size)
        self.color = [0,0,0]
        self.surf = pygame.Surface(self.size)
        self._x = 0
        self._y =0

    def setColor(self):
        self.color = choice(COLORS)
        self.surf.fill(self.color)

    def setSize(self):
        self.size = [randint(10,100),randint(10,100)]
        self.surf = pygame.Surface(self.size)
    def update(self,dict):
        if dict[K_UP]:
            self.goUp()
        if dict[K_DOWN]:
            self.goDown()
        if dict[K_LEFT]:
            self.goLeft()
        if dict[K_RIGHT]:
            self.goRight()
        if dict[K_SPACE]:
            self.setSize()
            self.setColor()
        
    def setRandomPosition(self):
        self.x = randint(0,WIDTH)
        self.y = randint(0,HEIGHT)

    def getPosition(self):
        position = [0,0]
        position[0] = self.x-(1/2*self.size[0])
        position[1] = self.y-(1/2*self.size[1])
        return position
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,other):
        """keeps object in bounds"""
        if other < 0:
            self._x = 0
        elif other >1000:
            self._x = 1000
        else:
            self._x = other
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,other):
        """keeps object in bounds"""
        if other < 0:
            self._y = 0
        elif other >750:
            self._y = 750
        else:
            self._y = other









########################### main game################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#####################################################################

# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a person object
p = Person()
RUNNING = True  # A variable to determine whether to get out of the
                # infinite game loop

while (RUNNING):
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            print(p)

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()
    
    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    p.update(pressedKeys)

    # fill the screen with a color
    screen.fill(WHITE)
    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()