
from kivy.app import App

# kivy.require("1.9.1")

from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window

from platform import Platform
from background import Background
from player import Player


from obstacles import Obstacles
        
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
        if self._check_hit():
            print("Game Over 1")
            return
            
        
        self.player.update()
        self.platform.update()
        self.background.update()
        self.obstacles.update()
        
    def _check_hit(self):
        condition1 = self.player.collide_widget(self.obstacles.image)
        condition2 = self.player.collide_widget(self.obstacles.image_dupe) 
        condition3 = self.player.collide_widget(self.obstacles.image_dupe2)
        condition4 = self.player.collide_widget(self.obstacles.image_dupe3) 
        return condition1 or condition2 or condition3 or condition4
        
        
        
class RunningMan(App):
    def build(self):
        game = Game()
        Window.size = game.size
        return game
    
    def update(self, *ignore):
        self.platform.update()
        self.background.update()
        self.obstacles.update()
        self.invis_obstacles.update()
            
if __name__ == "__main__":
    RunningMan().run()
    
    
    
    
    