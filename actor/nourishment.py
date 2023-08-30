import pygame
from actor.baseactor import BaseActor
class Nourishment(BaseActor):
    def step(self,screen:pygame.surface,actors:list):
        pygame.draw.circle(screen,(255,128,0),self.v2_to_v2int(self.pos),5)#イクラ描画
