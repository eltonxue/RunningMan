
from kivy.app import App

# kivy.require("1.9.1")

from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from platform import Platform
from background import Background
from player import Player


from obstacles import Obstacles


class StartScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class CreditsScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    
    def run_game(self):
        game = Game()
        return game

        
class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
        self.platform = Platform(source = "assets/platform/platform1.png")
        self.background = Background(source = "assets/background/meadow.png")

        self.player = Player(pos = (20,self.platform.height/2-5))

      
        self.obstacles = Obstacles(source = "assets/obstacles/box1.jpg")
        self.size = [1600 * .25, 900 * .25]
        
        
        self.add_widget(self.background)
        self.add_widget(self.platform)
        self.add_widget(self.player)
        self.add_widget(self.obstacles)
        Clock.schedule_interval(self.update, 1.0/60.0)
        

        
    def update(self, *ignores):
        self.player.update()
        self.platform.update()
        self.background.update()
        self.obstacles.update()
        
presentation = Builder.load_file("test_main.kv") 

class RunningMan(App):
#     def build(self):
#         game = Game()
#         Window.size = game.size
#         return game
    
    def build(self):
        Window.size = [1600 * .25, 900 * .25]
        return presentation  
    
    def update(self, *ignore):
        self.platform.update()
        self.background.update()
        self.obstacles.update()
        
        

# class StartMenu(App):
#     
#     def build(self):
#         Window.size = [1600 * .25, 900 * .25]
#         return presentation        


if __name__ == "__main__":

    RunningMan().run()
    
    
    
    
    