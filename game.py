import pandas as pd
import copy

black, white = [46/250, 64/250, 87/250,1], [246/250, 216/250, 174/250,1]

class Game:
    start_df = pd.DataFrame(data=[[0, 9, 0, 0, 0, 7, 5, 2, 0],
                                 [0, 0, 6, 8, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 3, 0, 9, 1, 0, 8],
                                 [2, 8, 0, 7, 0, 0, 0, 0, 0],
                                 [6, 0, 7, 0, 0, 0, 3, 8, 0],
                                 [0, 0, 0, 0, 0, 5, 0, 0, 2],
                                 [0, 0, 3, 5, 1, 0, 0, 0, 0],
                                 [8, 1, 0, 9, 7, 0, 4, 5, 3],
                                 [9, 6, 5, 4, 2, 0, 8, 0, 7]])
    ui_df = pd.DataFrame(data=[[None, None, None, None, None, None, None, None, None],
                                  [None, None, None, None, None, None, None, None, None],
                                  [None, None, None, None, None, None, None, None, None],
                                  [None, None, None, None, None, None, None, None, None],
                                  [None, None, None, None, None, None, None, None, None],
                                  [None, None, None, None, None, None, None, None, None],
                                  [None, None, None, None, None, None, None, None, None],
                                  [None, None, None, None, None, None, None, None, None],
                                  [None, None, None, None, None, None, None, None, None]])

    def __init__(self):
        self.solved_df = copy.deepcopy(self.start_df)
        self.game_df = copy.deepcopy(self.start_df)
        self.solve()

    def add_Button(self, i, j, button):
        value = self.game_df[i][j]
        if value > 0:
            button.text = str(value)
            button.disabled = True
        button.board_pos = (i,j)

    def get_cube_xy(self, i = None, j = None, n = None):
        x, y = 0, 0
        if not (i is None and j is None):
            if i >= 6:
                x = 6
            elif i >= 3:
                x = 3
            if j >= 6:
                y = 6
            elif j >= 3:
                y = 3
            return x, y
        elif not n is None:
            list = [ [0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2], #topleft cube
                     [3,0],[4,0],[5,0],[3,1],[4,1],[5,1],[3,2],[4,2],[5,2],
                     [6,0],[7,0],[8,0],[6,1],[7,1],[8,1],[6,2],[7,2],[8,2], #topright cube
                     [0,3],[1,3],[2,3],[0,4],[1,4],[2,4],[0,5],[1,5],[2,5],
                     [3,3],[4,3],[5,3],[3,4],[4,4],[5,4],[3,5],[4,5],[5,5], #middle cube
                     [6,3],[7,3],[8,3],[6,4],[7,4],[8,4],[6,5],[7,5],[8,5],
                     [0,6],[1,6],[2,6],[0,7],[1,7],[2,7],[0,8],[1,8],[2,8], #bottomleft cube
                     [3,6],[4,6],[5,6],[3,7],[4,7],[5,7],[3,8],[4,8],[5,8],
                     [6,6],[7,6],[8,6],[6,7],[7,7],[8,7],[6,8],[7,8],[8,8], #bottomright cube
                     ]
            return list[n][0], list[n][1]
        return None

    def solve(self, i = 0,j = 0):
        if i < 9:
            if j < 0:
                return self.solve(i-1, 8)
            elif j < 9:
                if self.solved_df[i][j] == 0:
                    for value in range(1,10):
                        x, y = self.get_cube_xy(i, j)
                        flag = True
                        for a in range(x, x + 3):
                            for b in range(y, y + 3):
                                if self.solved_df[a][b] == value:
                                    flag = False
                        # first condition for colunm
                        # second condition for row/line
                        if list(self.solved_df[i]).count(value) == 0 and \
                                list(self.solved_df.iloc[j]).count(value) == 0 and \
                                flag:

                            self.solved_df[i][j] = value
                            recurse = self.solve(i, j+1)
                            if not recurse is None:
                                return recurse
                            self.solved_df[i][j] = 0
                    else:
                        return None
                return self.solve(i, j+1)
            return self.solve(i+1, 0)
        return self.solved_df
