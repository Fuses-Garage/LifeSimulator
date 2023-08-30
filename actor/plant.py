import pygame
import random
from actor.baselife import BaseLife
from actor.nourishment import Nourishment
class Plant(BaseLife):
    def __init__(self, x: int, y: int,color=None) -> None:
        if color==None:
            color=self.calc_first_color()
        self.splittime=int(pygame.math.lerp(30,5,color[0]/255))
        self.splitrange=int(pygame.math.lerp(400,900,color[2]/255))
        super().__init__(x, y,pygame.math.lerp(50,200,color[1]/255),1,color)
    def step(self,screen:pygame.surface,actors:list):
        pygame.draw.polygon(screen,self.color,((self.pos.x-20,self.pos.y+30),(self.pos.x,self.pos.y-40),(self.pos.x+20,self.pos.y+30)))
        self.splittime-=1
        if self.splittime==0:
            n=list(filter(lambda x:isinstance(x,Nourishment) and(self.pos.x-x.pos.x)**2+(self.pos.y-x.pos.y)**2<=self.splitrange**2 ,actors))
            if len(n)>0:
                item=n[random.randint(0,len(n)-1)]
                item.alive=False
                actors.append(Plant(item.pos.x,item.pos.y,self.calc_next_color(self.color)))
            self.splittime=int(pygame.math.lerp(30,5,self.color[0]/255))
        super().step(screen)
