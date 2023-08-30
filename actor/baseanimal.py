import pygame
import random
from actor.baseactor import pygame
from actor.baselife import BaseLife
class BaseAnimal(BaseLife):
    def __init__(self, x: int, y: int, maxhealth: int, energy:int,sight:int,speed:int,color=None) -> None:
        if color==None:
            color=self.calc_first_color()
        self.vec = pygame.math.Vector2(1,1).rotate(random.random()*360)  #移動方向ベクトル
        self.sight:int=sight*pygame.math.lerp(0.75,2.5,color[2]/255)       #視界の半径
        self.speed:float=speed*pygame.math.lerp(0.75,3,color[0]/255)     #移動速度（最大）
        self.speedgear:float=1     #移動速度倍率
        self.target:BaseLife=None  #追いかけている対象
        super().__init__(x, y, maxhealth*pygame.math.lerp(0.75,2.5,color[1]/255), energy,color)
    def step(self, screen:pygame.surface,actors:list) -> None:
        self.health-=self.speedgear#速度倍率に応じ体力減少
        
        if(self.pos.y<=20 and self.vec.y<0):
            self.vec.y*=-1
        if(self.pos.y>=940 and self.vec.y>0):
            self.vec.y*=-1
        if(self.pos.x<=20 and self.vec.x<0):
            self.vec.x*=-1
        if(self.pos.x>=1260 and self.vec.x>0):
            self.vec.x*=-1
        self.pos+=self.vec.normalize()*self.speedgear*self.speed
        return super().step(screen)
    def get_insight(self,target:type,actors:list):
        #視界内のtarget型のアクタのリストを返す
        return list(filter(lambda x:(self.pos.x-x.pos.x)**2+(self.pos.y-x.pos.y)**2<=self.sight**2 and isinstance(x,target),actors))