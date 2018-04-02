import time
import random
import pygame
from syslogic import CGGPYG

class Life:
    def __init__(self):
        self.mtx=[]
        self.mtx2=[]
        self.cgg=CGGPYG()
        for i in range(0,40):
            for j in range(0,80):
                self.mtx[len(self.mtx):]=[random.randint(0,1)]
                self.mtx2[len(self.mtx2):]=[0]
    def move(self):
        for i in range(1,39):
            for j in range(1,79):
                ct=0
                if self.mtx[(i-1)*80+j-1]==1:
                    ct=ct+1
                if self.mtx[(i-1)*80+j]==1:
                    ct=ct+1
                if self.mtx[(i-1)*80+j+1]==1:
                    ct=ct+1
                if self.mtx[i*80+j-1]==1:
                    ct=ct+1
                if self.mtx[i*80+j+1]==1:
                    ct=ct+1
                if self.mtx[(i+1)*80+j-1]==1:
                    ct=ct+1
                if self.mtx[(i+1)*80+j]==1:
                    ct=ct+1
                if self.mtx[(i+1)*80+j+1]==1:
                    ct=ct+1
                if (ct==2 or ct==3) and self.mtx[i*80+j]==1 or ct==3 and self.mtx[i*80+j]==0:
                    self.mtx2[i*80+j]=1
                else:
                    self.mtx2[i*80+j]=0 
        for i in range(0,3200):
            self.mtx[i]=self.mtx2[i]

    def draw(self):
        self.cgg.cls()
        self.cgg.setcolor(7) 
        for i in range(1,39):
            for j in range(0,79):
                if self.mtx[i*80+j]==1:
                    self.cgg.put("star",j,i)
life=Life()
pygame.display.flip()
endflag=0
while endflag==0:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:endflag=1
    life.cgg.myclock.tick(60)   
    life.move()
    life.draw()
    pygame.display.flip()
    time.sleep(0.05)
pygame.quit()
