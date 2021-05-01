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
black, white, green, red = [41/250, 43/250, 44/250,1], [247/250, 247/250, 247/250,1],\
                           [92/250, 184/250, 92/250, 1],[217/250, 83/250, 79/250,1]

class MainScreen(Screen):
    pass
    # def __init__(self, **kwargs):
    #     super(MainScreen, self).__init__(**kwargs)


class QuickGame(Screen):
    board = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(QuickGame, self).__init__(**kwargs)
        self.game = Game()
        self.pressed = None

        Clock.schedule_once(self.make_board, 0.1)

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
        if self.pressed is button or button.text == '#':
            self.pressed = None
        else:
            button.color = white
            button.background_color = black
            button.background_normal= ''
            self.pressed = button

    def square_press(self, button):

        def reset_square(_):
            button.font_size -= 6
            button.bold = False

        if not self.pressed is None:
            value = self.pressed.text
            button.text = value
            self.numba_press(self.pressed)

            if int(button.text) == button.solved_value:
                button.color = green
            else:
                button.color = red
            button.font_size += 6
            button.bold = True

            Clock.schedule_once(reset_square, 2)


class ScreenManagement(ScreenManager):
    pass


presenataion = Builder.load_file('Main.kv')

class MainApp(App):
    def build(self):
        return presenataion

if __name__=='__main__':
    MainApp().run()