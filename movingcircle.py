import pygame
from pygame.locals import QUIT,KEYDOWN,K_UP,K_DOWN,K_LEFT,K_RIGHT
pygame.init()
WIDTH=600
HEIGHT=500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("moving circle")
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
abc=(0,0,156)

class Circle:
    def __init__(self,x,y,radius,color):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
     
    def draw(self,surface):
        pygame.draw.circle(surface,self.color,(self.x,self.y),self.radius)

    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy

    
circle=Circle(250,200,50,green)
running=True
while running:
    screen.fill(blue)
    circle.draw(screen)

    for event in pygame.event.get():
           if event.type==pygame.QUIT:
            running=False
           if event.type==KEYDOWN:
               if event.key==K_UP:
                   circle.move(0,-10)
               if event.key==K_DOWN:
                       circle.move(0,10)
               if event.key==K_LEFT:
                       circle.move(-10,0)
               if event.key==K_RIGHT:
                       circle.move(10,0)
    pygame.display.flip()
pygame.quit()

        

    
    



        
        
