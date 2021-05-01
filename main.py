import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.core.window import Window
from game import Game
import pandas as pd


Window.size = (350, 600)
kivy.require('2.0.0')
black, white = [46/250, 64/250, 87/250,1], [246/250, 216/250, 174/250,1]

class MainScreen(Screen):
    pass
    # def __init__(self, **kwargs):
    #     super(MainScreen, self).__init__(**kwargs)


class QuickGame(Screen):
    board = ObjectProperty(None)
    # btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9, btn_del = ObjectProperty(None), \
    # ObjectProperty(None),ObjectProperty(None),ObjectProperty(None),ObjectProperty(None),ObjectProperty(None), \
    # ObjectProperty(None),ObjectProperty(None),ObjectProperty(None),ObjectProperty(None)

    def __init__(self, **kwargs):
        super(QuickGame, self).__init__(**kwargs)
        self.game = Game()
        self.pressed = None

        Clock.schedule_once(self.make_board, 0.1)

    #     Clock.schedule_once(self.prnt, 0.5)
    #
    # def prnt(self, _):
    #     smth = self.game.ui_df.values.tolist()
    #     print(smth)

    def make_board(self,_):
        for i in range(0,9):
            box = BoxLayout(padding=[2,2])
            grid = GridLayout(cols=3)
            for j in range(0,9):
                    another_box = BoxLayout(padding=[.8,.8])
                    button = Button(color= black,
                                     background_color=white)

                    x, y = self.game.get_cube_xy(n=i * 9 + j)
                    button.bind(on_press = self.square_press)
                    self.game.add_Button(x, y, button)

                    another_box.add_widget(button)
                    grid.add_widget(another_box)
            box.add_widget(grid)
            self.board.add_widget(box)

    def numba_press(self, button):
        if not self.pressed is None:
            self.pressed.color = black
            self.pressed.background_color = white
            self.pressed.background_normal = ''
        if self.pressed is button:
            self.pressed = None
        else:
            button.color = white
            button.background_color = black
            button.background_normal= ''
            self.pressed = button

    def square_press(self, button):
        print(button.board_pos[0])
        if not self.pressed is None:
            value = self.pressed.text
            button.text = value
            self.numba_press(self.pressed)


class ScreenManagement(ScreenManager):
    pass


presenataion = Builder.load_file('Main.kv')

class MainApp(App):
    def build(self):
        return presenataion

if __name__=='__main__':
    MainApp().run()