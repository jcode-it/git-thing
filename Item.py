#####################################################################
# author: James Slayton
# date: 3/15/26
# description: 
#####################################################################
from math import sqrt
# global Constants to restrict the maximum x and y values that a person object
# can have.
MAX_X = 800
MAX_Y = 600

# A class representing a person. A person can be initialized with a
# name, as well as x and y coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). A person
# also has a size which is set to 1 by default. A person can go left, 
# go right, go up and go down. A person also has a string function 
# that prints out their name location, and size. A person also has a 
# function that calculates the euclidean distance from another person 
# object.
class Item:
    def __init__(self, name="player 1", x=0, y=0, size=1):
        self.name = name
        self.x = x
        self.y = y
        self.size = (size,size)

    def goLeft(self, distance=1):
        self.x = self.x - distance
    def goRight(self, distance=1):
        self.x = self.x + distance
    def goUp(self, distance=1):
        self.y = self.y - distance
    def goDown(self, distance=1):
        self.y = self.y + distance
    def getDistance(self, other: "Item"):
        result = sqrt((other.x - self.x)**2+(other.y - self.y)**2)
        return result
    def __str__(self):
        return f"x={self.x}\t y={self.y}\t size={self.size}"

