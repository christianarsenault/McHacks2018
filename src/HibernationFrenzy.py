import time
import pygame
import random


pygame.init()


displayWidth = 800
displayHeight = 600

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Hibernation Frenzy')

red = (210,0,0)
green = (0,210,0)
cyan = (0,255,255)
brightRed = (255,0,0)
brightGreen = (0,255,0)
yellow = (255,255,0)

black = (0,0,0)
white = (255,255,255)
apples_Fallen = 0
appleHeight = 96
speed = 8



clock = pygame.time.Clock()
catcherImg = pygame.image.load('../assets/catcher.png')
appleImg = pygame.image.load('../assets/applecropped.png')
backgroundImg = pygame.image.load('../assets/environment_forest.png')



def draw(fn,x,y):
    gameDisplay.blit(fn, (x,y))

def endGame(score,numToFinish):
    global apples_Fallen
    displayMessage('Finish!',0.5*displayWidth, 0.3*displayHeight,80, yellow)
    message = 'Score: ' + str(score) + '/' + str(numToFinish)
    displayMessage(message,0.5*displayWidth, 0.47*displayHeight,80, yellow)
    time.sleep(4)
    apples_Fallen = 0
    

def displayMessage(txt,x,y,fontSize,*color):
    font = pygame.font.Font('freesansbold.ttf',fontSize)
    surface, rect = textStuff(txt, font,color)
    rect.center = (x,y)
    gameDisplay.blit(surface, rect)
    pygame.display.update()
    
def textStuff(txt, font, color):
    surface = font.render(txt, True, color)
    return surface, surface.get_rect()

def gameIntro():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(cyan)
        text = pygame.font.SysFont("freesansbold.ttf",78)
        surface, rect = textStuff("Hibernation Frenzy", text,black)
        rect.center = ((displayWidth/2),(displayHeight*0.3))
        gameDisplay.blit(surface, rect)

        button("Start!",150,450,100,50,green,brightGreen,gameLoop)
        button("Quit",550,450,100,50,red,brightRed,quitGame)

        pygame.display.update()
        clock.tick(30)

def button(message,x,y,w,h,ic,ac,action=None):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > cursor[0] > x and y+h > cursor[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("freesansbold.ttf",20)
    surface, rect = textStuff(message, smallText, black)
    rect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(surface, rect)

def quitGame():
    pygame.quit()
    quit()

def gameLoop():
    applesToEnd = 50
    bearWidth = 176
    bearHeight = 189
    x_P1 =  (displayWidth * 0.5)-80
    y_P1 = (displayHeight * 0.6)
    score_P1 = 0
    startX = (displayWidth * 0.5)-80
    startY = (displayHeight * 0.6)

    mid = ((displayWidth * 0.5) - 40)
    right = ((displayWidth * 0.5) - 40) + (displayWidth * 0.07)
    left = ((displayWidth * 0.5) - 40) - (displayWidth * 0.07)

    bearLeft = False
    bearRight = False
    bearMid = True

    apple1X = mid
    apple1Y = -2000
    apple2X = left
    apple2Y = -990
    apple3X = right
    apple3Y = 0
    global apples_Fallen
    #choices for position of x for apples
    choices = [mid,left,right]

    #change background and let user prepare for carnage
    gameDisplay.fill(white)
    draw(backgroundImg,0,0)
    draw(catcherImg,x_P1,y_P1)
    

    
    

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == (pygame.K_a):
                    x_P1 -=  (displayWidth * 0.07)
                elif event.key == pygame.K_d:
                    x_P1 +=  (displayWidth * 0.07)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    x_P1 +=  (displayWidth * 0.07)
                elif event.key == pygame.K_d:
                    x_P1 -=  (displayWidth * 0.07)
                    
       
        
        

        gameDisplay.fill(white)
        draw(backgroundImg,0,0)
        draw(catcherImg,x_P1,y_P1)
        draw(appleImg,apple1X,apple1Y)
        draw(appleImg,apple2X,apple2Y)
        draw(appleImg,apple3X,apple3Y)

        apple1Y += speed
        apple2Y += speed
        apple3Y += speed

        scoreSentence = 'Score: ' + str(score_P1)
        #displayMessage(txt,x,y,fontSize,*color):
        displayMessage(scoreSentence, 100,90,25,brightRed)

        if(apples_Fallen == applesToEnd):
                endGame(score_P1,applesToEnd)
                break;

        #collision handling

        if(x_P1 == startX):
            bearMid = True
            bearLeft = False
            bearRight = False
        if(x_P1 == startX+(displayWidth * 0.07)):
            bearRight = True
            bearLeft = False
            bearMid = False
        if(x_P1 == startX-(displayWidth * 0.07)):
            bearMid = False
            bearLeft = True
            bearRight = False
        if((apple1X == mid and bearMid) or (apple1X == left and bearLeft) or (apple1X == right and bearRight)):
            if(apple1Y >= y_P1+bearHeight*0.25):     
                score_P1 += 1
                apples_Fallen += 1
                if(apples_Fallen >= 48):
                    apple1Y = -7000            
                elif(apples_Fallen<48):
                    apple1Y = 200 - appleHeight
                    apple1X = random.choice(choices)
        if((apple2X == mid and bearMid) or (apple2X == left and bearLeft) or (apple2X == right and bearRight)):
            if(apple2Y >= y_P1+bearHeight*0.25):
                score_P1 += 1
                apples_Fallen += 1
                if(apples_Fallen >= 48):
                    apple2Y = -7000            
                elif(apples_Fallen<48):
                    apple2Y = 200 - appleHeight
                    apple2X = random.choice(choices)

        if((apple3X == mid and bearMid) or (apple3X == left and bearLeft) or (apple3X == right and bearRight)):
            if(apple3Y >= y_P1+bearHeight*0.25):
                score_P1 += 1
                apples_Fallen += 1
                if(apples_Fallen >= 48):
                    apple3Y = -7000            
                elif(apples_Fallen<48):
                    apple3Y = 200 - appleHeight
                    apple3X = random.choice(choices)
        if(apple1Y > y_P1+bearHeight*0.25):
            apples_Fallen += 1
            if(apples_Fallen >= 48):
                    apple1Y = -7000            
            elif(apples_Fallen<48):
                apple1Y = 200 - appleHeight
                apple1X = random.choice(choices)
        if(apple2Y > y_P1+bearHeight*0.25):
            apples_Fallen += 1
            if(apples_Fallen >= 48):
                    apple2Y = -7000            
            elif(apples_Fallen<48):
                apple2Y = 200 - appleHeight
                apple2X = random.choice(choices)
        if(apple3Y > y_P1+bearHeight*0.25):
            apples_Fallen += 1
            if(apples_Fallen >= 48):
                    apple3Y = -7000            
            elif(apples_Fallen<48):
                apple3Y = 200 - appleHeight
                apple3X = random.choice(choices)


            
        pygame.display.update()
        clock.tick(60)
gameIntro()
gameLoop()
pygame.quit()
quit()
