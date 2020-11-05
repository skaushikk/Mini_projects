#Snake Tutorial Python
import numpy 
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
 
class board(object):
    rows = 25
    w = 500
    def __init__(self,start,dnx=1,dny=0,color=(255,210,0)):
        self.pos = start
        self.dnx = 1
        self.dny = 0
        self.color = color
 
        
    def move(self, dnx, dny):
        self.dnx = dnx
        self.dny = dny
        self.pos = (self.pos[0] + self.dnx, self.pos[1] + self.dny)
 
    def draw(self, surface, eyes=False):
        d = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
 
        pygame.draw.rect(surface, self.color, (i*d+1,j*d+1, d-2, d-2))
        if eyes:
            centre = d//2
            radius = 3
            eye1 = (i*d+centre-radius,j*d+8)
            eye2 = (i*d + d -radius*2, j*d+8)
            pygame.draw.circle(surface, (0,0,255), eye1, radius)
            pygame.draw.circle(surface, (0,0,255), eye2, radius)
        
 
 
 
class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = board(pos)
        self.body.append(self.head)
        self.dnx = 0
        self.dny = 1
 
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
 
            keys = pygame.key.get_pressed()
 
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dnx = -1
                    self.dny = 0
                    self.turns[self.head.pos[:]] = [self.dnx, self.dny]
 
                elif keys[pygame.K_RIGHT]:
                    self.dnx = 1
                    self.dny = 0
                    self.turns[self.head.pos[:]] = [self.dnx, self.dny]
 
                elif keys[pygame.K_UP]:
                    self.dnx = 0
                    self.dny = -1
                    self.turns[self.head.pos[:]] = [self.dnx, self.dny]
 
                elif keys[pygame.K_DOWN]:
                    self.dnx = 0
                    self.dny = 1
                    self.turns[self.head.pos[:]] = [self.dnx, self.dny]
 
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dnx,c.dny)
        
 
    def reset(self, pos):
        self.head = board(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dnx = 0
        self.dny = 1
 
 
    def add(self):
        tail = self.body[-1]
        dx, dy = tail.dnx, tail.dny
 
        if dx == 1 and dy == 0:
            self.body.append(board((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(board((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(board((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(board((tail.pos[0],tail.pos[1]+1)))
 
        self.body[-1].dnx = dx
        self.body[-1].dny = dy
        
 
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i ==0:
                c.draw(surface, True)
            else:
                c.draw(surface)
 
 
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
 
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
 
        pygame.draw.line(surface, (255,255,0), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,0), (0,y),(w,y))
        
 
def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0,0,0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width,rows, surface)
    pygame.display.update()
 
 
def randomSnack(rows, item):
 
    positions = item.body
 
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
        
    return (x,y)
 
 
def message_box_(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass
 
 
def main():
    global width, rows, s, snack
    width = 500
    rows = 25
    win = pygame.display.set_mode((width, width))
    s = snake((0,255,0), (10,10))
    snack = board(randomSnack(rows, s), color=(0,255,0))
    flag = True
 
    clock = pygame.time.Clock()
    
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        if s.body[0].pos == snack.pos:
            s.add()
            snack = board(randomSnack(rows, s), color=(0,255,0))
 
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print('Score: ', len(s.body))
                message_box_('You Lose!', 'hahaha')
                s.reset((10,10))
                break
 
            
        redrawWindow(win)
 
        
    pass
 
 
 
main()