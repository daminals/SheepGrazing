from random import choice

class Sheep:    
    def __init__(self,x,y,col):
        self.x = x
        self.y = y
        self.sz = 10
        self.col = col
        self.energy = 20
        self.age = 0
        if self.col == YELLOW:
            self.energy = 47
        
    def update(self):   
        rows_of_grass = height/patchSize 
        move = 7
        if (self.col == PURPLE):
            move = 12
        self.energy -= 1
        if self.energy <= 0:
            sheepList.remove(self)
        if self.energy >= 50 or (self.energy >= 35 and self.col == WHITE):
            self.sexyTimes()
        self.x += random(-move,move)
        self.y += random(-move,move)
        if self.x > width:
            self.x %= width;
        if self.y > height:
            self.y %= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
            
        xscl = int(self.x / patchSize)
        yscl = int(self.y / patchSize)
        grass = grassList[xscl * rows_of_grass + yscl]
        if not grass.eaten:
            self.energy+=grass.energy
            if (self.col == RED):
                self.energy += 3
            grass.eaten = True
        fill(self.col)
        ellipse(self.x,self.y,self.sz,self.sz)
        self.age += 1
        self.death()
        if devMode:
            self.thicc()
        
    def sexyTimes(self):
        self.energy -= 30
        sheepList.append(Sheep(self.x,self.y,self.col))
        self.age += 5
        if (self.col == WHITE):
            for i in range(2):
                sheepList.append(Sheep(self.x,self.y,self.col))
    
    def death(self):
        if (random(100)+self.age >= 150):
            if self in sheepList:
                sheepList.remove(self)
                
    def thicc(self):
        self.sz = self.energy//2


class Grass:
    def __init__(self,x,y,sz):
        self.x = x
        self.y = y
        self.energy = 5
        self.eaten = False
        self.sz = sz
    def update(self):
        if (self.eaten):
            if random(100) < 5:
                self.eaten = False
            else:
                fill(BROWN)
        else:
            fill(GREEN)
        noStroke()
        rect(self.x,self.y,self.sz,self.sz)


sheepList = []
grassList = []
patchSize = 10
WHITE = color(255)
BROWN = color(102,51,0)
RED = color(255,0,0)
GREEN = color(0,102,0)
YELLOW = color(255,255,0)
PURPLE = color(102,0,204)
col_list = [WHITE,RED,YELLOW,PURPLE]

devMode = False


def setup():
    global patchSize
    size(600,600)
    global row_of_grass
    for i in range(20):
        sheepList.append(Sheep(random(width),random(height),choice(col_list)))
        
    for i in range(0,width,patchSize):
        for j in range(0,height,patchSize):
            grassList.append(Grass(i,j,patchSize))
    
def draw():
    background(255)
    for grass in grassList:
        grass.update()
    for sheep in sheepList:
        sheep.update()
      
def keyPressed(SPACE):
    global devMode
    if devMode:
        devMode = False
    else:
        devMode = True
