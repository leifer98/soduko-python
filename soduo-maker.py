print('type here:')
a = list(input())
list = [[7,0,6,0,0,0,0,8,0],
          [0,0,2,1,0,0,0,0,6],
          [0,0,0,0,0,0,0,0,7],
          [0,9,0,0,0,0,3,5,0],
          [8,0,0,5,0,0,0,0,0],
          [0,1,0,0,2,0,0,0,0],
          [0,0,0,2,7,6,0,0,0],
          [0,0,0,0,0,1,8,0,9],
          [0,0,0,0,0,8,4,0,0]]

for i in range(0,9):
    for j in range(0,9):
        print(i,j,  int(i*9 + j))
        # print(list[i])
        # list[i].append(int(a[x]))
        list[i][j] = int(a[(int(i*9 + j))])
# list[5].append(3)
# list[6].append(3)
print(a)
print(list)
