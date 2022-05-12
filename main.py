import pygame
import random
pygame.init()#initiale the game screen
screen = pygame.display.set_mode((800,800))#the game screen
xpos = 0
ypos = 0
mousePos = (xpos, ypos)#mouse postion variable to be able to check the location of the mouse
RGB = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
RGB1 = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
RGB2 = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
RGB3 = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
RGB4 = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
rndmclrs = [RGB, RGB1, RGB2, RGB3, RGB4]
draw = False
#the color variables ---------

color = (rndmclrs[0],rndmclrs[1],rndmclrs[2])
#--------------------------------

#class function prints the rndmclrs color boxes to the screen-------
class colors:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen, (rndmclrs[0]), (self.xpos,self.ypos+750,50,50))
        pygame.draw.rect(screen, (rndmclrs[1]), (self.xpos+50 ,self.ypos+750,50,50))
        pygame.draw.rect(screen, (rndmclrs[2]), (self.xpos+100,self.ypos+750,50,50))
        pygame.draw.rect(screen, (rndmclrs[3]), (self.xpos+150,self.ypos+750,50,50))
        pygame.draw.rect(screen, (rndmclrs[4]), (self.xpos+200,self.ypos+750,50,50))
       
       
colors1=colors(0,0)
colors1.draw()
#------------------------------------------------------------------

#the game loop--------------------------------------------------------
while True:
   

    #mouse input---------------------------------------------------
    for event in pygame.event.get():#partner israel helped with game loop bugs specifically this line  
        if event.type == pygame.MOUSEBUTTONDOWN:#CLICK
            mousePos = event.pos
        #I used an old assignment given to me from my teacher as a referance peice (lines 55-65)
        #checks if mouse has been clicked
        if event.type == pygame.MOUSEBUTTONDOWN:  
                draw = True

        if event.type == pygame.MOUSEBUTTONUP:
                draw = False

               
        if event.type == pygame.QUIT: #close game
            break

    #part of this next section I used old assignment/base code for a referance peice(lines68-83)-------
    if mousePos[0] > 0 and mousePos[0] < 50 and mousePos[1] >750:
         color = (rndmclrs[0])
    if mousePos[0] > 50 and mousePos[0] < 100 and mousePos[1] >750:#partner alexander helped with a bug that wasnt checking mouse position
        color = (rndmclrs[1])
    if mousePos[0] > 100 and mousePos[0] < 150 and mousePos[1] >750:
         color = (rndmclrs[2])
    if mousePos[0] > 150 and mousePos[0] < 200 and mousePos[1] >750:
         color = (rndmclrs[3])
    if mousePos[0] > 200 and mousePos[0] < 250 and mousePos[1] >750:
         color = (rndmclrs[4])
    if mousePos[0] > 250 and mousePos[0] < 300 and mousePos[1] >750:#partnenr alexander helped with adding the eraser
         color = (0,0,0)
         
    #draws the circles to the screen where mouse is located    
    if draw == True:  
        pygame.draw.circle(screen, (color), (mousePos), 10)
    pygame.draw.rect(screen, (255,255,255), (250, 750, 50,50), 5)
    #------------------------------------------------------------------------


    pygame.display.flip()
   
#------end of game loop-------

pygame.quit
