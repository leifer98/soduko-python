import pygame, time, copy, math

pygame.init()
width, height, fps = 450, 450, 10 # change fps to make solution loops speed
width, height = 600, 600
surface = pygame.display.set_mode((width,height))
pygame.display.set_caption('Soduko')
clock, start_ticks = pygame.time.Clock(), pygame.time.get_ticks()
pressed = pygame.key.get_pressed()
black, white, red, green, blue, gray = (0,0,0), (255,255,255), (255,0,0), (0,255,0), (0,0,255), (50,50,50)
reverted, solved = [], []
score = 0

# hard
# matrix = [[7,0,6,0,0,0,0,8,0],
#           [0,0,2,1,0,0,0,0,6],
#           [0,0,0,0,0,0,0,0,7],
#           [0,9,0,0,0,0,3,5,0],
#           [8,0,0,5,0,0,0,0,0],
#           [0,1,0,0,2,0,0,0,0],
#           [0,0,0,2,7,6,0,0,0],
#           [0,0,0,0,0,1,8,0,9],
#           [0,0,0,0,0,8,4,0,0]]
# medium
matrix = [[0,0,5,1,0,0,0,7,0],
          [7,3,4,0,0,8,0,0,1],
          [0,0,9,7,0,0,0,3,5],
          [0,2,6,8,0,1,0,4,0],
          [0,0,0,0,0,0,6,2,0],
          [4,0,3,0,5,6,1,9,0],
          [0,6,0,4,2,7,3,1,0],
          [0,0,0,0,0,3,0,5,0],
          [3,4,0,9,1,0,0,8,0]]


def upside(matrix):
    opp = []
    for x in range(9):
        temp = []
        for y in range(9):
            temp += [matrix[y][x]]
        opp = opp + [temp]
    return opp



def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return  textSurface, textSurface.get_rect()  #power of python returning 2 objects

def cleanup():
    for i in range(9):
        for j in range(9):
            if matrix[i][j] > 9:
                matrix[i][j] = matrix[i][j] - 10

def square(posX,posY,value = 0):
    global score, start_ticks
    pygame.draw.rect(surface, white, (posX * width / 9, posY * height / 9, width / 9, height / 9), 2)
    mouse = pygame.mouse.get_pos()
    if (posX * width / 9) + (width / 9)>mouse[0]>(posX * width / 9) and \
            (posY * height / 9) + (height / 9)>mouse[1]>(posY * height / 9):
        pygame.draw.rect(surface, gray, (posX * width / 9, posY * height / 9, width / 9, height / 9), 0)
        if pygame.mouse.get_pressed()[0] and reverted[posX][posY] == 0:
            if value<10:
                cleanup()
                value = value + 10

    if not value % 10 == 0:
        largeText = pygame.font.Font('freesansbold.ttf', int(height / 15))
        textSurf, textRect = text_objects(str(value % 10), largeText, white)
        if not solved == []: # only for solution loops
            if not value%10 == solved[posX][posY]:
                textSurf, textRect = text_objects(str(value % 10), largeText, red)
        textRect.center = ((posX * width / 9) + ((width / 9) / 2), (posY * height / 9) + ((height / 9) / 2) + 3)
        surface.blit(textSurf, textRect)
    if value > 19:
        value = value - 10
    elif value > 9:
        # print(value, (posX,posY))
        pygame.draw.rect(surface, red, (posX * width / 9 + 3, posY * height / 9 + 3, width / 9 - 6, height / 9 - 6),
                     2)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_1] or pressed[pygame.K_KP1]:
            value = 1
            if not value == solved[posX][posY]:
                score = score - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000))
                start_ticks = pygame.time.get_ticks()
            elif not matrix[posX][posY] % 10 == value:
                score = max(score + 150 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                start_ticks = pygame.time.get_ticks()
        elif pressed[pygame.K_2] or pressed[pygame.K_KP2]:
            value = 2
            if not value == solved[posX][posY]:
                score = score - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000))
                start_ticks = pygame.time.get_ticks()
            elif not matrix[posX][posY] % 10 == value:
                score = max(score + 150 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                start_ticks = pygame.time.get_ticks()
        elif pressed[pygame.K_3] or pressed[pygame.K_KP3]:
            value = 3
            if not value == solved[posX][posY]:
                score = score - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000))
                start_ticks = pygame.time.get_ticks()
            elif not matrix[posX][posY] % 10 == value:
                score = max(score + 150 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                start_ticks = pygame.time.get_ticks()
        elif pressed[pygame.K_4] or pressed[pygame.K_KP4]:
            value = 4
            if not value == solved[posX][posY]:
                score = score - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000))
                start_ticks = pygame.time.get_ticks()
            elif not matrix[posX][posY] % 10 == value:
                score = max(score + 150 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                start_ticks = pygame.time.get_ticks()
        elif pressed[pygame.K_5] or pressed[pygame.K_KP5]:
            value = 5
            if not value == solved[posX][posY]:
                score = score - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000))
                start_ticks = pygame.time.get_ticks()
            elif not matrix[posX][posY] % 10 == value:
                score = max(score + 150 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                start_ticks = pygame.time.get_ticks()
        elif pressed[pygame.K_6] or pressed[pygame.K_KP6]:
            value = 6
            if not value == solved[posX][posY]:
                score = score - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000))
                start_ticks = pygame.time.get_ticks()
            elif not matrix[posX][posY] % 10 == value:
                score = max(score + 150 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                start_ticks = pygame.time.get_ticks()
        elif pressed[pygame.K_7] or pressed[pygame.K_KP7]:
            value = 7
            if not value == solved[posX][posY]:
                score = score - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000))
                start_ticks = pygame.time.get_ticks()
            elif not matrix[posX][posY] % 10 == value:
                score = max(score + 150 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                start_ticks = pygame.time.get_ticks()
        elif pressed[pygame.K_8] or pressed[pygame.K_KP8]:
            value = 8
            if not value == solved[posX][posY]:
                score = score - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000))
                start_ticks = pygame.time.get_ticks()
            elif not matrix[posX][posY] % 10 == value:
                score = max(score + 150 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                start_ticks = pygame.time.get_ticks()
        elif pressed[pygame.K_9] or pressed[pygame.K_KP9]:
            value = 9
            if not value == solved[posX][posY]:
                score = score - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000))
            elif not matrix[posX][posY] % 10 == value:
                score = max(score + 150 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
        elif pressed[pygame.K_UP] and posY>0:
            if reverted[posX][posY-1] == 0:
                value = value - 10
                matrix[posX][posY-1] = matrix[posX][posY-1] + 20
        elif pressed[pygame.K_DOWN] and posY<8:
            if reverted[posX][posY+1] == 0:
                value = value - 10
                matrix[posX][posY+1] = matrix[posX][posY+1] + 20
        elif pressed[pygame.K_LEFT] and posX>0:
            if reverted[posX-1][posY] == 0:
                value = value - 10
                matrix[posX-1][posY] = matrix[posX-1][posY] + 20
        elif pressed[pygame.K_RIGHT] and posX<8:
            if reverted[posX+1][posY] == 0:
                value = value - 10
                matrix[posX+1][posY] = matrix[posX+1][posY] + 20
        elif pressed[pygame.K_SPACE] or pressed[pygame.K_0] or pressed[pygame.K_KP0] or pressed[pygame.K_DELETE] or pressed[pygame.K_BACKSPACE] :
            value -= 10

    return value

def scorer():
    largeText = pygame.font.SysFont('britannic', int(height / 5))
    textSurf, textRect = text_objects(str(score), largeText, white)
    textSurf.set_alpha(150)
    textRect.center = (width/2, width - width/10)
    surface.blit(textSurf, textRect)

def timer():
    seconds = int((pygame.time.get_ticks() - start_ticks) / 1000)
    largeText = pygame.font.SysFont('britannic', int(height / 5))
    string = str(seconds)
    if seconds > 59 :
        minutes = int(seconds / 60)
        seconds = seconds % 60
        string = str(minutes) + ':' + str(seconds)
        if seconds<10:
            string = str(minutes) + ':0' + str(seconds)
    textSurf, textRect = text_objects(string, largeText, white)
    textSurf.set_alpha(150)
    textRect.center = (width / 2, width/10)
    surface.blit(textSurf, textRect)

def loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    surface.fill(black)
    for i in range(9):
        for j in range(9):
            matrix[i][j] = square(i,j,matrix[i][j])

    for i in range(1,3):
        pygame.draw.line(surface,red,(i*width/3-1,0),(i*width/3-1,height),4)
        pygame.draw.line(surface,red,(0,i*height/3-1),(width,i*height/3-1),4)

    scorer()
    timer()

    pygame.display.update()
    clock.tick(fps)

def solve(matrix,i,j):
    # uncomment to see resolving loops
    # loop()
    if i < 9:
        if j < 9:
            if matrix[i][j] == 0:
                for x in range(1,10):
                    if matrix[i].count(x) == 0:
                        flag = True
                        for y in matrix:
                            if y[j] == x:
                                flag = False

                        kube_x, kube_y = 6, 6
                        if j < 3:
                            kube_y = 0
                        elif j < 6:
                            kube_y = 3
                        if i < 3:
                            kube_x = 0
                        elif i < 6:
                            kube_x = 3
                        for a in range(kube_x,kube_x+3):
                            for b in range(kube_y,kube_y+3):
                                if x == matrix[a][b]:
                                    flag = False

                        if flag:
                            matrix[i][j] = x
                            sol = solve(matrix, i, j + 1)
                            if not sol is None:
                                return sol
                            matrix[i][j] = 0
                return None
            return solve(matrix, i, j + 1)
        else:
            return solve(matrix, i+1, 0)
    else:
        return matrix

matrix = upside(matrix)
reverted = copy.deepcopy(matrix)
solve(matrix,0,0)
solved = copy.deepcopy(matrix)
# comment to see the solved version
matrix = copy.deepcopy(reverted)
while True:
    loop()

pygame.quit()
quit()