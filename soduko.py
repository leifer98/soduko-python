import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

kivy.require('2.0.0')

class MainScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class DrawInput(Widget):
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