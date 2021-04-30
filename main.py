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
Window.size = (350, 600)
kivy.require('2.0.0')

class MainScreen(Screen):
    pass
    # def __init__(self, **kwargs):
    #     super(MainScreen, self).__init__(**kwargs)


class QuickGame(Screen):
    board = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(QuickGame, self).__init__(**kwargs)
        Clock.schedule_once(self.make_board, 0.1)

    def make_board(self,_):
        for i in range(1,10):
            self.box = BoxLayout(padding=[2,2])
            self.grid = GridLayout(cols=3)
            for j in range(1,10):
                    self.another_box = BoxLayout(padding=[.8,.8])
                    self.button = Button(text=str(j),
                                         color= [0,0,0,1],
                                         background_color=[1,1,1,1],
                                         background_normal= '')
                    self.another_box.add_widget(self.button)
                    self.grid.add_widget(self.another_box)
            self.box.add_widget(self.grid)
            self.board.add_widget(self.box)


class ScreenManagement(ScreenManager):
    pass


presenataion = Builder.load_file('Main.kv')

class MainApp(App):
    def build(self):
        return presenataion

if __name__=='__main__':
    MainApp().run()