import pygame
import random
from actor.baseactor import *
class BaseLife(BaseActor):
    def __init__(self,x:int,y:int,maxhealth:int,energy=1,color=(85,85,85)) -> None:
        self.maxhealth=maxhealth
        self.health=maxhealth
        self.energy=energy
        self.color=color
        super().__init__(x,y)
    def step(self, screen:pygame.surface) -> None:
        self.health-=0.3
        self.maxhealth-=0.2
        if self.health<=0:
            self.die()
        super().step(screen)
    def heal(self,value:int):
        self.health=min(self.health+value,self.maxhealth)
    def die(self):
        self.health=0
        self.maxhealth=0
        self.alive=False
    def eaten(self):
        self.energy=0
        self.die()
    def calc_first_color(self):
        r=0
        g=0
        b=0
        for _ in range(400):
            rand=random.randint(0,2)
            if rand==0:
                r+=1
            elif rand==1:
                g+=1
            elif rand==2:
                b+=1
        return(r,g,b)
    def calc_next_color(self,parentcol:tuple):
        r=parentcol[0]-10
        g=parentcol[1]-10
        b=parentcol[2]-10
        for _ in range(30):
            rand=random.randint(0,2)
            if rand==0:
                r+=1
            elif rand==1:
                g+=1
            elif rand==2:
                b+=1
        return(r,g,b)