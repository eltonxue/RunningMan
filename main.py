
from kivy.app import App

# kivy.require("1.9.1")

from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window

from platform import Platform
from background import Background
from player import Player


class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
        self.platform = Platform(source = "assets/platform/platform1.png")
        self.background = Background(source = "assets/background/meadow.png")
        self.player = Player(pos = (20,self.platform.height/2-5))
        self.size = [1600 * .25, 900 * .25]
        
        
        self.add_widget(self.background)
        self.add_widget(self.platform)
        self.add_widget(self.player)
        Clock.schedule_interval(self.update, 1.0/60.0)
        
    def update(self, *ignores):
        self.player.update()
        self.platform.update()
        self.background.update()
        
        
        
class RunningMan(App):
    def build(self):
        game = Game()
        Window.size = game.size
        return game
    
    def update(self, *ignore):
        self.platform.update()
        self.background.update()


if __name__ == "__main__":
    RunningMan().run()
    
    
    
    
    