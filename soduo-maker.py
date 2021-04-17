while True:
    print('type here:')
    a = list(input())
    list1 = [[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0]]
    x = 0
    print('[', end='')
    for i in range(9):
        for j in range(9):
            list1[i][j] = int(a[x])
            x += 1
    for x in list1:
        if list1[8] is x:
            print(x, end='] \n')
        else:
            print(x, end=', \n')
