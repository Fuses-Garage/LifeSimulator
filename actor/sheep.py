import pygame
from actor.baseanimal import BaseAnimal
class Sheep(BaseAnimal):
    def __init__(self, x: int, y: int,color=None) -> None:
        super().__init__(x, y,200,4,200,1.5,color)
        self.speedgear=0.5
        self.escapetime=0#逃亡状態が解除される時間
        self.vdangervec=pygame.Vector2(0,0)
    def step(self,screen:pygame.surface,actors:list):
        if self.time>45:#重なり防止のため、最初の1.5秒はランダム方向に直進させる
            from actor.wolf import Wolf
            from actor.plant import Plant
            self.speedgear=0.8
            danger=self.get_insight(Wolf,actors)#視界内の天敵のリスト
            verydanger=filter(lambda x:x.target==self,self.get_insight(Wolf,actors))#自分を狙う天敵のリスト
            food=self.get_insight(Plant,actors)#視界内の飯のリスト
            dangervec=pygame.Vector2(0,0)
            foodvec=pygame.Vector2(0,0)
            for v in danger:
                dangervec+=(self.pos-v.pos)*(self.sight/max(1,(v.pos-self.pos).magnitude()))
            if((dangervec.length()>0)):
                dangervec=dangervec.normalize()
            for v in verydanger:
                self.vdangervec+=(self.pos-v.pos)
                self.escapetime=self.time+15#逃亡開始
            if self.escapetime>self.time:
                self.speedgear=1
            else:
                self.vdangervec=pygame.Vector2(0,0)#逃亡終了
            if(self.vdangervec.length()>0):
                self.vdangervec=self.vdangervec.normalize()*5
            if len(food)>0:
                food.sort(key=lambda x:(self.pos-x.pos).length())#距離が短い順に並べる
                foodvec+=(food[0].pos-self.pos)*(self.sight/max(1,(food[0].pos-self.pos).magnitude()))
                self.target=food[0]
                foodvec=foodvec.normalize()*3
                if(self.target!=None):#捕食対象を追いかけているなら
                    if (self.pos-self.target.pos).length()<20:#至近距離なら
                        self.energy+=self.target.energy
                        self.target.eaten()
                        self.heal(300)
                        if(self.energy>=8):#十分なエネルギーがあるなら
                            while self.energy>=8:
                                self.energy-=4
                                actors.append(Sheep(self.pos.x,self.pos.y,self.calc_next_color(self.color)))
            if (foodvec+dangervec+self.vdangervec).length()>0:
                self.vec=(foodvec+dangervec+self.vdangervec).normalize()
        pygame.draw.rect(screen,self.color,(self.pos.x-20,self.pos.y-20,40,40))
        super().step(screen,actors)