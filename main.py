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
from kivy.animation import Animation
from kivy.core.window import Window
from game import Game
import pandas as pd


Window.size = (350, 600)
kivy.require('2.0.0')
black, white, green, red = [0.164, 0.172, 0.176, 1], [0.988, 0.988, 0.988, 1],\
                           [0.368, 0.736, 0.368, 1],[0.868, 0.332, 0.316, 1]

class MainScreen(Screen):
    pass
    # def __init__(self, **kwargs):
    #     super(MainScreen, self).__init__(**kwargs)


class WarmUpScreen(Screen, Game):
    board, pop_up_message = ObjectProperty(None), ObjectProperty(None)
    score_label, changed_score_label, time_label, del_btn = ObjectProperty(None), ObjectProperty(None), \
                                                 ObjectProperty(None), ObjectProperty(None)

    def __init__(self, **kwargs):
        super(WarmUpScreen, self).__init__(**kwargs)
        self.setup_new_game()

    def setup_new_game(self, *args):
        self.number_pressed,self.square_pressed = None,None
        self.time,self.score,self.time_limit = -1,0,15  # to change timelimit

        Clock.schedule_once(self.make_board,0)
        self.clock = Clock.schedule_interval(self.update_time,1)
        self.clock.cancel()  # comment if you starting from this screen

    def update_score(self, change):
        self.score += change
        self.score_label.text = str(self.score)
        if change > 0:
            self.changed_score_label.text = '+'+str(change)
            self.changed_score_label.color = green
        else:
            self.changed_score_label.text = str(change)
            self.changed_score_label.color = red

        self.popup_anim(self.changed_score_label)
        self.popup_anim(self.score_label)


    def update_time(self, *args):
        if self.time >= self.time_limit:
            self.time = -1
            self.update_score(-100)
        elif self.time >= self.time_limit-6:
            self.popup_anim(self.time_label)

        self.time += 1

        min = int(self.time / 60)
        sec = int(self.time % 60)
        text = ''
        if min > 9:
            text = str(min)+ ':'
        else:
            text = '0'+str(min)+':'
        if sec > 9:
            text += str(sec)
        else:
            text += '0'+str(sec)

        self.time_label.text = text

    def make_board(self, *args):
        for i in range(0,9):
            box = BoxLayout(padding=[2,2])
            grid = GridLayout(cols=3)
            for j in range(0,9):
                    another_box = BoxLayout(padding=[.8,.8])
                    button = Button(color= black,
                                     background_color=white)

                    x, y = self.get_cube_xy(n=i * 9 + j)
                    button.bind(on_press = self.square_press)
                    self.add_Button(x, y, button)

                    another_box.add_widget(button)
                    grid.add_widget(another_box)
            box.add_widget(grid)
            self.board.add_widget(box)

    def popup_anim(self, widget):
        font_size = widget.font_size
        anim_end = Animation(font_size=font_size,duration=0.2)
        anim_start = Animation(font_size=font_size+5,duration=0.2)

        anim_start.bind(on_complete=lambda *args: Clock.schedule_once(lambda *args: anim_end.start(widget),0.2))

        anim_start.start(widget)

    def numba_press(self, button):
        if not self.number_pressed is None:
            self.btn_unpress(self.number_pressed)

        if self.number_pressed is button or button.text == '#':
            if not self.square_pressed is None:
                self.btn_unpress(self.square_pressed)
                self.square_pressed = None
            self.number_pressed = None

        elif self.square_pressed is None:
            self.btn_press(button)
            self.number_pressed = button
        else:
            self.btn_unpress(self.square_pressed)
            self.number_pressed = button
            self.square_press(self.square_pressed)

    def btn_press(self, button):
        button.color = white
        button.background_color = black

    def btn_unpress(self, button):
        button.color = black
        button.background_color = white

    def square_press(self, button):

        if not self.number_pressed is None:
            value = self.number_pressed.text
            button.text = value

            i, j = button.board_pos
            self.game_df[i][j] = value

            self.btn_unpress(self.number_pressed)
            self.number_pressed = None
            self.square_pressed = None

            if int(button.text) == button.solved_value:
                button.disabled = True
                button.color = green

                change = max(100 - (5*self.time), 25)
                self.update_score(change)

            else:
                button.color = red

                change = -min(5*self.time, 50)
                self.update_score(change)
            self.popup_anim(button)
            self.time = 0

        elif self.square_pressed is None:
            self.btn_press(button)
            self.square_pressed = button
        else:
            self.btn_unpress(self.square_pressed)
            if self.square_pressed is button:
                self.square_pressed = None
            else:
                self.btn_press(button)
                self.square_pressed = button


class ScreenManagement(ScreenManager):
    pass


presenataion = Builder.load_file('Main.kv')

class MainApp(App):
    def build(self):
        return presenataion

if __name__=='__main__':
    MainApp().run()