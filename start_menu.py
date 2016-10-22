from kivy.app import App
from kivy.lang import Builder
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
#from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition



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


# class Widgets(Widget):
#     pass


# class StartScreen(GridLayout):
#     def __init__(self, **kwargs):
#         super(StartScreen, self).__init__(**kwargs)
#         self.cols = 2
#         
#         self.add_widget(Label(text = "Username:"))
#         self.username = TextInput(multiline=False)
#         self.add_widget(self.username)
#         
#         self.add_widget(Label(text = "Password:"))
#         self.password = TextInput(multiline=False, password=True)
#         self.add_widget(self.password)


presentation = Builder.load_file("start_menu.kv")

from kivy.core.window import Window

class StartMenu(App):
    
    def build(self):
        Window.size = [1600 * .25, 900 * .25]
        return presentation
    
    
if __name__ == "__main__":
    
    StartMenu().run()