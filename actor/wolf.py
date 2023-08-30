import pygame
from actor.baseanimal import *
class Wolf(BaseAnimal):
    def __init__(self, x: int, y: int,color=None) -> None:
        super().__init__(x, y,400,20,200,1.5,color)
        self.speedgear=0.5
    def step(self,screen:pygame.surface,actors:list):
        from actor.sheep import Sheep
        if self.time>45:
            self.speedgear=0.3
            food=self.get_insight(Sheep,actors)#視界内の飯のリスト
            foodvec=pygame.Vector2(0,0)
            if self.health/max(self.maxhealth,0.1)<1 and len(food)>0:
                food.sort(key=lambda x:(self.pos-x.pos).length())
                foodvec+=(food[0].pos-self.pos)*(self.sight/max(1,(food[0].pos-self.pos).magnitude()))
                self.target=food[0]
                if(foodvec.length()>0):
                    foodvec=foodvec.normalize()
                    self.speedgear=1.0
                    if(self.target!=None):
                        if (self.pos-self.target.pos).length()<20:
                            self.energy+=self.target.energy
                            self.target.eaten()
                            self.heal(300)
                            if(self.energy>=40):
                                while self.energy>=40:
                                    self.energy-=20
                                    actors.append(Wolf(self.pos.x,self.pos.y,self.calc_next_color(self.color)))
            if (foodvec).length()>0:
                self.vec=(foodvec).normalize()
        pygame.draw.polygon(screen,self.color,(self.pos+(20,0),self.pos+(0,20),self.pos+(-20,0),self.pos+(0,-20)))
        super().step(screen,actors)