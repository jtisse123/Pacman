from pygame import Rect
from pygame.math import Vector2

import core


class Pac_man:
    def __init__(self,x=300,y=200):
        self.defautPos=Vector2(x,y)
        self.position=Vector2(x,y)
        self.vel = Vector2(random.uniform(-10,10),random.uniform(-10,10))
        self.couleur =(200,200,200)
        self.rayon=10