import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button

kivy.require('2.0.0')

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'main'
        def func(_):
            self.parent.current = 'quickgame'
        self.qg_button = Button(text = 'Quick Game',
                                font_size = self.height/3,
                                size_hint = (0.8,0.2),
                                pos_hint = {'right':0.9,'top':0.8},
                                on_release = func)
        self.add_widget(self.qg_button)

    # Button:
    #     on_release: app.root.current = 'quickgame'


class QuickGame(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class Board(Widget):
    def on_touch_down(self, touch):
        # print(touch)
        with self.canvas:
            touch.ud['line'] = Line(points=(touch.x,touch.y))
    def on_touch_move(self, touch):
        # print(touch)
        touch.ud['line'].points += (touch.x,touch.y)
    def on_touch_up(self, touch):
        # print(touch)
        pass

presenataion = Builder.load_file('Main.kv')

class MainApp(App):
    def build(self):
        return presenataion

if __name__=='__main__':
    MainApp().run()