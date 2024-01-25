#initialization
import pygame
pygame.init()

#resolution & captions
screen_x = 1050
screen_y = 600

screen = pygame.display.set_mode((screen_x,screen_y))
title = pygame.display.set_caption("Pybrush")

#colour codings
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (127,127,127)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
PINK = (255,0,255)
YELLOW = (255,255,0)
BLOOD = (100,0,0)

screen.fill(WHITE)

#classes
class bar:
    def __init__(self,x,y,position,a,b,size,COLOUR):
        self.x = x
        self.y = y
        self.position = x,y
        self.a = a
        self.b = b
        self.size = a,b
        self.COLOUR = COLOUR

class colour:
    def __init__(self,x,y,position,a,b,size,COLOUR):
        self.x = x
        self.y = y
        self.position = x,y
        self.a = a
        self.b = b
        self.size = a,b
        self.COLOUR = COLOUR

class canvas:
    def __init__(self,x,y,position,a,b,size,COLOUR):
        self.x = x
        self.y = y
        self.position = x,y
        self.a = a
        self.b = b
        self.size = a,b
        self.COLOUR = COLOUR

class brush:
    def __init__(self,x,y,position,a,b,size,COLOUR):
        self.x = x
        self.y = y
        self.position = x,y
        self.a = a
        self.b = b
        self.size = a,b
        self.COLOUR = COLOUR

class frame:
    def __init__(self,x,y,position,a,b,size,COLOUR,w):
        self.x = x
        self.y = y
        self.position = x,y
        self.a = a
        self.b = b
        self.size = a,b
        self.COLOUR = COLOUR
        self.w = w

class eraser:
    def __init__(self,x,y,position,a,b,size,COLOUR):
        self.x = x
        self.y = y
        self.position = x,y
        self.a = a
        self.b = b
        self.size = a,b
        self.COLOUR = COLOUR

#image loading
banner = pygame.image.load("banner.bmp")

#other variable assigning
colour_a = 30
colour_b = 30
colour_size = colour_a,colour_b

id1 = "black"
buffer1 = "none1"
id2 = "circle"
buffer2 = "none2"

radius = 2
size = [radius*2,radius*2]
rubber_size = 20,20

choice = BLACK
lt = ["black","white","red","green","blue","cyan","pink","yellow"]
draw = False

#properties assigning
belt = bar(0,0,(0,0),screen_x,100,(screen_x,100),GREY)

black = colour(screen_x-60,10,(screen_x-60,10),colour_a,colour_b,(colour_size),BLACK)
white = colour(screen_x-100,10,(screen_x-100,10),colour_a,colour_b,(colour_size),WHITE)
red = colour(screen_x-140,10,(screen_x-140,10),colour_a,colour_b,(colour_size),RED)
green = colour(screen_x-180,10,(screen_x-180,10),colour_a,colour_b,(colour_size),GREEN)
blue = colour(screen_x-60,50,(screen_x-60,50),colour_a,colour_b,(colour_size),BLUE)
cyan = colour(screen_x-100,50,(screen_x-100,50),colour_a,colour_b,(colour_size),CYAN)
pink = colour(screen_x-140,50,(screen_x-140,50),colour_a,colour_b,(colour_size),PINK)
yellow = colour(screen_x-180,50,(screen_x-180,50),colour_a,colour_b,(colour_size),YELLOW)

strip1 = bar(screen_x-210,0,(screen_x-210,0),3,belt.b,(3,belt.b),BLACK)

board = canvas(0,belt.b,(0,belt.b),screen_x,screen_y-100,(screen_x,screen_y-100),WHITE)

square = brush(100,20,(100,20),60,60,(60,60),BLACK)
circle = brush(50,50,(50,50),30,30,(30,30),BLACK)

strip2 = bar(square.x+90,0,(square.x+90,0),3,belt.b,(3,belt.b),BLACK)
strip3 = bar((screen_x/2)+50,0,((screen_x/2)+50,0),3,belt.b,(3,belt.b),BLACK)

rubber = eraser(strip1.x-100,20,(strip1.x-100,20),70,40,(70,40),WHITE)
refill = bar(strip3.x+20,0,(strip3.x+20,0),strip3.a*7,strip3.b,(strip3.a*7,strip3.b),RED)

frame1 = frame(black.x,black.y,(black.x,black.y),black.a,black.b,(black.a,black.b),BLOOD,4)
frame2 = frame(square.x,square.y,(square.x,square.y),square.a,square.b,(square.a,square.b),BLOOD,4)

#drawing shapes
pygame.draw.rect(screen,belt.COLOUR,(belt.position,belt.size))

pygame.draw.rect(screen,black.COLOUR,(black.position,black.size))
pygame.draw.rect(screen,white.COLOUR,(white.position,white.size))
pygame.draw.rect(screen,red.COLOUR,(red.position,red.size))
pygame.draw.rect(screen,green.COLOUR,(green.position,green.size))
pygame.draw.rect(screen,blue.COLOUR,(blue.position,blue.size))
pygame.draw.rect(screen,cyan.COLOUR,(cyan.position,cyan.size))
pygame.draw.rect(screen,pink.COLOUR,(pink.position,pink.size))
pygame.draw.rect(screen,yellow.COLOUR,(yellow.position,yellow.size))

pygame.draw.rect(screen,strip1.COLOUR,(strip1.position,strip1.size))

pygame.draw.rect(screen,board.COLOUR,(board.position,board.size))

pygame.draw.rect(screen,square.COLOUR,(square.position,square.size))
pygame.draw.circle(screen,circle.COLOUR,(circle.position),circle.a)

pygame.draw.rect(screen,strip2.COLOUR,(strip2.position,strip2.size))
pygame.draw.rect(screen,strip3.COLOUR,(strip3.position,strip3.size))

pygame.draw.rect(screen,rubber.COLOUR,(rubber.position,rubber.size))
pygame.draw.rect(screen,refill.COLOUR,(refill.position,refill.size))

screen.blit(banner,(strip2.x+30,strip2.y+15))

siri = frame2.x-80,frame2.y

pygame.draw.rect(screen,frame1.COLOUR,(frame1.position,frame1.size),frame1.w)
pygame.draw.rect(screen,frame2.COLOUR,(siri,frame2.size),frame2.w)

#display update
pygame.display.update()

#event loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                if radius < 9:
                    radius += 1
                    size[0] = radius*2
                    size[1] = radius*2
                    
            elif event.key == pygame.K_RCTRL:
                if radius > 1:
                    radius -= 1
                    size[0] = radius*2
                    size[1] = radius*2
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if x>black.x and x<black.x+black.a and y>black.y and y<black.y+black.b:
                buffer1 = id1
                id1 = "black"

            elif x>white.x and x<white.x+white.a and y>white.y and y<white.y+white.b:
                buffer1 = id1
                id1 = "white"
                
            elif x>red.x and x<red.x+red.a and y>red.y and y<red.y+red.b:
                buffer1 = id1
                id1 = "red"
                
            elif x>green.x and x<green.x+green.a and y>green.y and y<green.y+green.b:
                buffer1 = id1
                id1 = "green"
                
            elif x>blue.x and x<blue.x+blue.a and y>blue.y and y<blue.y+blue.b:
                buffer1 = id1
                id1 = "blue"
                
            elif x>cyan.x and x<cyan.x+cyan.a and y>cyan.y and y<cyan.y+cyan.b:
                buffer1 = id1
                id1 = "cyan"
                
            elif x>pink.x and x<pink.x+pink.a and y>pink.y and y<pink.y+pink.b:
                buffer1 = id1
                id1 = "pink"
                
            elif x>yellow.x and x<yellow.x+yellow.a and y>yellow.y and y<yellow.y+yellow.b:
                buffer1 = id1
                id1 = "yellow"

            elif x>rubber.x and x<rubber.x+rubber.a and y>rubber.y and y<rubber.y+rubber.b:
                buffer1 = id1
                id1 = "rubber"

            elif x>refill.x and x<refill.x+refill.a and y>refill.y and y<refill.y+refill.b:
                pygame.draw.rect(screen,board.COLOUR,(board.position,board.size))
                pygame.display.update()

            elif x>frame2.x-80 and x<frame2.x-80+frame2.a and y>frame2.y and y<frame2.y+frame2.b:
                buffer2 = id2
                id2 = "circle"

            elif x>square.x and x<square.x+square.a and y>square.y and y<square.y+square.b:
                buffer2 = id2
                id2 = "square"

            if buffer1 == "black":
                pygame.draw.rect(screen,black.COLOUR,(black.position,black.size))
                pygame.display.update()

            if buffer1 == "white":
                pygame.draw.rect(screen,white.COLOUR,(white.position,white.size))
                pygame.display.update()

            if buffer1 == "red":
                pygame.draw.rect(screen,red.COLOUR,(red.position,red.size))
                pygame.display.update()

            if buffer1 == "green":
                pygame.draw.rect(screen,green.COLOUR,(green.position,green.size))
                pygame.display.update()

            if buffer1 == "blue":
                pygame.draw.rect(screen,blue.COLOUR,(blue.position,blue.size))
                pygame.display.update()

            if buffer1 == "cyan":
                pygame.draw.rect(screen,cyan.COLOUR,(cyan.position,cyan.size))
                pygame.display.update()

            if buffer1 == "pink":
                pygame.draw.rect(screen,pink.COLOUR,(pink.position,pink.size))
                pygame.display.update()

            if buffer1 == "yellow":
                pygame.draw.rect(screen,yellow.COLOUR,(yellow.position,yellow.size))
                pygame.display.update()

            if buffer1 == "rubber":
                pygame.draw.rect(screen,rubber.COLOUR,(rubber.position,rubber.size))
                pygame.display.update()

            if id1 == "black":
                pygame.draw.rect(screen,frame1.COLOUR,(black.position,frame1.size),frame1.w)
                pygame.display.update()

            if id1 == "white":
                pygame.draw.rect(screen,frame1.COLOUR,(white.position,frame1.size),frame1.w)
                pygame.display.update()

            if id1 == "red":
                pygame.draw.rect(screen,frame1.COLOUR,(red.position,frame1.size),frame1.w)
                pygame.display.update()

            if id1 == "green":
                pygame.draw.rect(screen,frame1.COLOUR,(green.position,frame1.size),frame1.w)
                pygame.display.update()

            if id1 == "blue":
                pygame.draw.rect(screen,frame1.COLOUR,(blue.position,frame1.size),frame1.w)
                pygame.display.update()

            if id1 == "cyan":
                pygame.draw.rect(screen,frame1.COLOUR,(cyan.position,frame1.size),frame1.w)
                pygame.display.update()

            if id1 == "pink":
                pygame.draw.rect(screen,frame1.COLOUR,(pink.position,frame1.size),frame1.w)
                pygame.display.update()

            if id1 == "yellow":
                pygame.draw.rect(screen,frame1.COLOUR,(yellow.position,frame1.size),frame1.w)
                pygame.display.update()

            if id1 == "rubber":
                pygame.draw.rect(screen,frame1.COLOUR,(rubber.position,rubber.size),frame1.w)
                pygame.display.update()

            if buffer2 == "circle":
                pygame.draw.rect(screen,GREY,(siri,frame2.size),frame2.w)
                pygame.display.update()

            if buffer2 == "square":
                pygame.draw.rect(screen,square.COLOUR,(square.position,square.size))
                pygame.display.update()

            if id2 == "circle":
                pygame.draw.rect(screen,frame2.COLOUR,(siri,frame2.size),frame2.w)
                pygame.display.update()
                
            if id2 == "square":
                pygame.draw.rect(screen,frame2.COLOUR,(frame2.position,frame2.size),frame2.w)
                pygame.display.update()

            if x>board.x and x<board.x+board.a and y>board.y and y<board.y+board.b:
                draw = True
                
                if id1 == "black":
                    choice = BLACK

                elif id1 == "white":
                    choice = WHITE

                elif id1 == "red":
                    choice = RED

                elif id1 == "green":
                    choice = GREEN

                elif id1 == "blue":
                    choice = BLUE

                elif id1 == "cyan":
                    choice = CYAN

                elif id1 == "pink":
                    choice = PINK

                elif id1 == "yellow":
                    choice = YELLOW

                elif id1 == "rubber":
                    choice = WHITE

        elif event.type == pygame.MOUSEBUTTONUP:
            draw = False

        elif event.type == pygame.MOUSEMOTION:
            region = event.pos
            x = event.pos[0]
            y = event.pos[1]
            
            if draw == True and (x>board.x and x<board.x+board.a and y>board.y and y<board.y+board.b) == True:
                if id1 in lt:
                    if id2 == "circle":
                        pygame.draw.circle(screen,choice,(region),radius)
                        pygame.display.update()

                    elif id2 == "square":
                        pygame.draw.rect(screen,choice,(region,size))
                        pygame.display.update()

                elif id1 == "rubber":
                    pygame.draw.rect(screen,choice,(region,rubber_size))##################################
                    pygame.display.update()
                    
#final update & quit
pygame.display.update()
pygame.quit()
