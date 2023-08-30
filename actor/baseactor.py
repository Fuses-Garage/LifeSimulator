import pygame
class BaseActor():
    def __init__(self,x:int,y:int) -> None:
        self.pos = pygame.math.Vector2(min(max(x,0),1280),min(max(y,0),960))  #座標
        self.alive:bool=True#アクタは生きているか？
        self.time=0
    def step(self,screen:pygame.surface)->None:
        self.time+=1
        pass
    def v2_to_v2int(self,v:pygame.math.Vector2): 
        return(round(v.x.__float__()), round(v.y.__float__())) 