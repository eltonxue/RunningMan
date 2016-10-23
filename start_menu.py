from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
#from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from main import RunningMan
from kivy.uix.button import Button


class StartScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class CreditsScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


class TouchInput(Widget):
     
    def on_touch_down(self, touch):
        pass
         
    def on_touch_move(self, touch):
        pass   
         
    def on_touch_up(self, touch):
        pass



presentation = Builder.load_file("start_menu.kv")

from kivy.core.window import Window

class StartMenu(App):
    
    def build(self):
        Window.size = [1600 * .25, 900 * .25]
        return presentation
    
    
if __name__ == "__main__":
    
    StartMenu().run()