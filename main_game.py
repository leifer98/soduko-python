import pygame
import time, random

pygame.init()

display_width, display_height, car_width, car_height, buttons = 800, 600, 73, 82, []
black, white, red, green, blue = (0,0,0), (255,255,255), (255,0,0), (0,255,0), (0,0,255)
light_red, light_green, light_blue = (255,100,100), (100,255,100), (100,100,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Soduko')
clock = pygame.time.Clock()

carImg = pygame.image.load('../pygame tutorial/racecar.png') #transpernt using gimp

def button(thingColor,thingX,thingY,thingW,thingH,string,textSize, func = None, hover = False):
    largeText = pygame.font.Font('freesansbold.ttf', textSize)
    textSurf, textRect = text_objects(string, largeText)
    textRect.center = (thingX+(thingW / 2), thingY+(thingH / 2))

    if [string,func,[thingX,thingX+thingW,thingY,thingY+thingH],not hover] in buttons:
        if thingColor == blue:
            thingColor = light_blue
        if thingColor == red:
            thingColor = light_red
    elif not [string,func,[thingX,thingX+thingW,thingY,thingY+thingH],hover] in buttons:
        buttons.append([string,func,[thingX,thingX+thingW,thingY,thingY+thingH],hover])

    pygame.draw.rect(gameDisplay, thingColor, [thingX, thingY, thingW, thingH])
    gameDisplay.blit(textSurf, textRect)

def Bquit():
    pygame.quit()
    quit()

def dodged_count(count):
    font = pygame.font.SysFont(None,25)
    text = font.render('Dodged: '+str(count),True,black)
    gameDisplay.blit(text, (0,0))

def things(thingX,thingY,thingW,thingH,thingColor):
    pygame.draw.rect(gameDisplay, thingColor, [thingX,thingY,thingW,thingH])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return  textSurface, textSurface.get_rect()  #power of python returning 2 objects

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    textSurf, textRect = text_objects(text, largeText)
    textRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed !')

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEMOTION:
                # possible shorter with pygame.mouse.get_pos()
                for b in buttons:
                    if b[2][1] > event.pos[0] > b[2][0] and b[2][3] > event.pos[1] > b[2][2]:
                        # []string,func,[thingX,thingX+thingW,thingY,thingY+thingH],hover]
                        b[3] = True
                    elif b[3]:
                        buttons.remove(b)
            if event.type == pygame.MOUSEBUTTONUP:
                for b in buttons:
                    if b[2][1] > event.pos[0] > b[2][0] and b[2][3] > event.pos[1] > b[2][2]:
                        if b[1] is not None:
                            b[1]()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        textSurf, textRect = text_objects('Soduko', largeText)
        textRect.center = ((display_width * 0.5), (display_height * 0.35))
        gameDisplay.blit(textSurf, textRect)
        # button(thingColor,thingX,thingY,thingW,thingH,string,textSize, func = None):
        button(blue,display_width*0.2,display_height*0.8,100,50,'start',35,game_loop)
        button(red,display_width*0.7,display_height*0.8,100,50,'quit',35,Bquit)
        pygame.display.update()
        clock.tick(60)

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    thing_height, thing_width, thing_speed, score = 100, 100, 3, 0
    thing_startY, thing_startX = -600, random.randrange(0, display_width-thing_width)
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            # print(event) # types all events occured, great for event and idea discovery!

        x += x_change
        gameDisplay.fill(white)
        # things(thingX,thingY,thingW,thingH,thingColor) , nice way to comment and help
        things(thing_startX,thing_startY,thing_width,thing_height,black)
        thing_startY += thing_speed
        car(x,y)
        dodged_count(score)
        if x > (display_width-car_width) or x < 0:
            crash()
        if thing_startY > (display_height):
            thing_startY = -600
            thing_startX = random.randrange(0, display_width-thing_width)
            score += 1
            thing_speed += 0.75

        # look what you hav done son and what u shouldve done below....
        # if (thing_startX < x < thing_startX+thing_width and
        #     thing_startY < y <thing_startY+thing_height) or \
        #         (thing_startX < (x+car_width) < thing_startX + thing_width and
        #          thing_startY < (y+car_height) < thing_startY + thing_height) or \
        #         (thing_startX < (x+car_width) < thing_startX+thing_width and
        #     thing_startY < y <thing_startY+thing_height) or \
        #         (thing_startX < x < thing_startX + thing_width and
        #          thing_startY < (y+car_height) < thing_startY + thing_height):
        #     crash()

        if y < thing_startY+thing_height:
            if thing_startX<x<thing_startX+thing_width or \
                    thing_startX<x+car_width<thing_startX+thing_width:
                crash()

        pygame.display.update()
        clock.tick(60)
game_intro()
pygame.quit()
quit()