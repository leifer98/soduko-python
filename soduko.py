import pygame, time, copy, math, sodukodata

pygame.init()
width, height, fps = 450, 450, 30 # change fps to make solution loops speed
width, height = 600, 600
surface = pygame.display.set_mode((width,height))
pygame.display.set_caption('Soduko')
clock, start_ticks = pygame.time.Clock(), pygame.time.get_ticks()
pressed = pygame.key.get_pressed()
black, white, red, green, blue, gray = (55, 62, 64), (183, 213, 212), (239, 111, 108), (63, 125, 32), (131, 128, 182), (119, 135, 139)
reverted, solved = [], []
score, delay, winloss, = 0, 0, True
player, score2, pause = False, 0, False

data_object = sodukodata.Data()
matrix = data_object.random_matrix()

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
    global score, start_ticks, delay, winloss, score2
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
        pygame.draw.rect(surface, red, (posX * width / 9 + 3, posY * height / 9 + 3, width / 9 - 6, height / 9 - 6),
                     2)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_1] or pressed[pygame.K_KP1]:
            value = 1
            if not value == solved[posX][posY]:
                change = max(50,30 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)))
                if not player:
                    score -= change
                else:
                    score2 -= change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = False
            elif not matrix[posX][posY] % 10 == value:
                change = max(100 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                if not player:
                    score += change
                else:
                    score2 += change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = True

        elif pressed[pygame.K_2] or pressed[pygame.K_KP2]:
            value = 2
            if not value == solved[posX][posY]:
                change = max(50,30 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)))
                if not player:
                    score -= change
                else:
                    score2 -= change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = False
            elif not matrix[posX][posY] % 10 == value:
                change = max(100 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                if not player:
                    score += change
                else:
                    score2 += change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = True

        elif pressed[pygame.K_3] or pressed[pygame.K_KP3]:
            value = 3
            if not value == solved[posX][posY]:
                change = max(50,30 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)))
                if not player:
                    score -= change
                else:
                    score2 -= change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = False
            elif not matrix[posX][posY] % 10 == value:
                change = max(100 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                if not player:
                    score += change
                else:
                    score2 += change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = True

        elif pressed[pygame.K_4] or pressed[pygame.K_KP4]:
            value = 4
            if not value == solved[posX][posY]:
                change = max(50,30 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)))
                if not player:
                    score -= change
                else:
                    score2 -= change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = False
            elif not matrix[posX][posY] % 10 == value:
                change = max(100 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                if not player:
                    score += change
                else:
                    score2 += change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = True

        elif pressed[pygame.K_5] or pressed[pygame.K_KP5]:
            value = 5
            if not value == solved[posX][posY]:
                change = max(50,30 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)))
                if not player:
                    score -= change
                else:
                    score2 -= change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = False
            elif not matrix[posX][posY] % 10 == value:
                change = max(100 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                if not player:
                    score += change
                else:
                    score2 += change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = True

        elif pressed[pygame.K_6] or pressed[pygame.K_KP6]:
            value = 6
            if not value == solved[posX][posY]:
                change = max(50,30 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)))
                if not player:
                    score -= change
                else:
                    score2 -= change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = False
            elif not matrix[posX][posY] % 10 == value:
                change = max(100 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                if not player:
                    score += change
                else:
                    score2 += change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = True

        elif pressed[pygame.K_7] or pressed[pygame.K_KP7]:
            value = 7
            if not value == solved[posX][posY]:
                change = max(50,30 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)))
                if not player:
                    score -= change
                else:
                    score2 -= change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = False
            elif not matrix[posX][posY] % 10 == value:
                change = max(100 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                if not player:
                    score += change
                else:
                    score2 += change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = True

        elif pressed[pygame.K_8] or pressed[pygame.K_KP8]:
            value = 8
            if not value == solved[posX][posY]:
                change = max(50,30 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)))
                if not player:
                    score -= change
                else:
                    score2 -= change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = False
            elif not matrix[posX][posY] % 10 == value:
                change = max(100 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                if not player:
                    score += change
                else:
                    score2 += change
                delay = ((pygame.time.get_ticks() - start_ticks)/1000)
                start_ticks = pygame.time.get_ticks()
                winloss = True

        elif pressed[pygame.K_9] or pressed[pygame.K_KP9]:
            value = 9
            if not value == solved[posX][posY]:
                change = max(50,30 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)))
                if not player:
                    score -= change
                else:
                    score2 -= change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = False
            elif not matrix[posX][posY] % 10 == value:
                change = max(100 - 10 * int(math.sqrt((pygame.time.get_ticks() - start_ticks)/1000)), 20)
                if not player:
                    score += change
                else:
                    score2 += change
                delay = ((pygame.time.get_ticks() - start_ticks) / 1000)
                start_ticks = pygame.time.get_ticks()
                winloss = True

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
        elif pressed[pygame.K_0] or pressed[pygame.K_KP0] or pressed[pygame.K_DELETE] or pressed[pygame.K_BACKSPACE] :
            value -= 10

    return value

def scorer():
    global delay, start_ticks
    largeText = pygame.font.SysFont('britannic', int(height / 5))
    textSurf, textRect = text_objects(str(score), largeText, blue)
    textSurf.set_alpha(150)
    largeText2 = pygame.font.SysFont('britannic', int(height / 5))
    textSurf2, textRect2 = text_objects(str(score2), largeText2, blue)
    textSurf2.set_alpha(150)

    if not player:
        if delay > 0:
            largeText = pygame.font.SysFont('britannic', int(height / 4))
            if winloss:
                textSurf, textRect = text_objects(str(score), largeText, green)
            else:
                textSurf, textRect = text_objects(str(score), largeText, red)
    else:
        if delay > 0:
            largeText2 = pygame.font.SysFont('britannic', int(height / 4))
            if winloss:
                textSurf2, textRect2 = text_objects(str(score2), largeText2, green)
            else:
                textSurf2, textRect2 = text_objects(str(score2), largeText2, red)

    textRect.center = (width / 4, width - width / 10)
    surface.blit(textSurf, textRect)
    textRect2.center = (width - width / 4, width - width / 10)
    surface.blit(textSurf2, textRect2)

def timer():
    global delay, start_ticks, player
    seconds = int((pygame.time.get_ticks() - start_ticks) / 1000)
    if delay > 0:
        temp = seconds
        seconds = math.ceil(delay)
        if not temp < 3:
            delay = 0
            start_ticks = pygame.time.get_ticks()
            player = not player

    string, string2 = str(seconds), '0'
    if player:
        string2, string = str(seconds), '0'
    if seconds > 59 :
        minutes = int(seconds / 60)
        seconds = int(seconds % 60)
        string = str(minutes) + ':' + str(seconds)
        if seconds<10:
            string = str(minutes) + ':0' + str(seconds)

    largeText = pygame.font.SysFont('britannic', int(height / 5))
    textSurf, textRect = text_objects(string, largeText, blue)
    textSurf.set_alpha(150)

    largeText2 = pygame.font.SysFont('britannic', int(height / 5))
    textSurf2, textRect2 = text_objects(string2, largeText2, blue)
    textSurf2.set_alpha(150)

    if not player:
        if delay > 0:
            largeText = pygame.font.SysFont('britannic', int(height / 4))
            if winloss:
                textSurf, textRect = text_objects(string, largeText, green)
            else:
                textSurf, textRect = text_objects(string, largeText, red)
    else:
        if delay > 0:
            largeText2 = pygame.font.SysFont('britannic', int(height / 4))
            if winloss:
                textSurf2, textRect2 = text_objects(string2, largeText2, green)
            else:
                textSurf2, textRect2 = text_objects(string2, largeText2, red)

    textRect.center = (width / 4, width / 10)
    surface.blit(textSurf, textRect)
    textRect2.center = (width - width / 4, width / 10)
    surface.blit(textSurf2, textRect2)

def loop():
    global start_ticks, pause
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if (pause and ((pygame.time.get_ticks() - start_ticks) / 1000) > 3) or not pause:
                pause = not pause
                start_ticks = pygame.time.get_ticks()

    surface.fill(black)
    for i in range(9):
        for j in range(9):
            matrix[i][j] = square(i,j,matrix[i][j])

    for i in range(1,3):
        pygame.draw.line(surface,red,(i*width/3-1,0),(i*width/3-1,height),4)
        pygame.draw.line(surface,red,(0,i*height/3-1),(width,i*height/3-1),4)

    scorer()
    timer()
    if pause:
        surface.fill(black)
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