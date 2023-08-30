import sys, random
import pygame
from actor.baselife import BaseLife
from actor.nourishment import Nourishment
from actor.plant import Plant
from actor.sheep import Sheep
from actor.wolf import Wolf
from pygame.locals import *
pygame.init()#pygame初期化
clock = pygame.time.Clock()
pygame.display.set_caption("生態系シミュ")
screen = pygame.display.set_mode((1280,960))
tuti = (90,60,30)#土の色（茶色）
actors=[]
for _ in range(75):
    actors.append(Nourishment(random.randint(20,1260),random.randint(20,940)))#養分を30個
for _ in range(15):
    actors.append(Plant(random.randint(20,1260),random.randint(20,940)))#植物を10個
for _ in range(5):
    actors.append(Sheep(random.randint(20,1260),random.randint(20,940)))#草食を8匹
for _ in range(1):
    actors.append(Wolf(random.randint(20,1260),random.randint(20,940)))#肉食を2匹

while True:
    screen.fill(tuti)#背景を塗る
    
    for v in actors:
        v.step(screen,actors)#アクターの処理
    removelist=filter(lambda x:not x.alive,actors)
    for v in removelist:
        if isinstance(v,BaseLife):
            for _ in range(v.energy):
                actors.append(Nourishment(v.pos.x+random.randrange(-70,70),v.pos.y+random.randrange(-70,70)))#生物除去時エネルギーを落とす
        actors.remove(v)
    pygame.display.update()#描画更新
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(30)#30FPS