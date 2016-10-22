
from kivy.app import App

# kivy.require("1.9.1")

from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window

from platform import Platform
        
class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
        self.platform = Platform(source = "assets/platform/platform1.png")
        self.size = [1600 * .10, 900 * .10]
        
        self.add_widget(self.platform)
        Clock.schedule_interval(self.update, 1.0/60.0)
        
    def update(self, *ignores):
        self.platform.update()
        
        
class RunningMan(App):
    def build(self):
        game = Game()
        Window.size = game.size
        return game
    
    def update(self, *ignore):
        self.platform.update()


if __name__ == "__main__":
    RunningMan().run()
    
    
    
    
    