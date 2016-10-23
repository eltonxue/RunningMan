
from kivy.app import App

# kivy.require("1.9.1")

from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.label import Label

from platform import Platform
from background import Background
from player import Player
from invis_player import InvisPlayer


from obstacles import Obstacles
from invis_obstacles import InvisObstacles


class Score(Label):
    def __init__(self, score, font_name, font_size):
        self.score = score
        self.score_board = Label(text = score, font_name = font_name, font_size = font_size)
        
    def update(self):
        pass
        
        
class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
        self.platform = Platform(source = "assets/platform/platform1.png")
        self.background = Background(source = "assets/background/meadow.png")

        self.player = Player(pos = (20, self.platform.height/2 - 5))
        self.invis_player = InvisPlayer(pos = (100, self.platform.height + 20))
      
        self.obstacles = Obstacles(source = "assets/obstacles/box1.jpg")
        self.invis_obstacles = InvisObstacles(source = "assets/obstacles/box1.jpg")
        
        self.size = [1600 * .25, 900 * .25]

        
        self.add_widget(self.background)
        self.add_widget(self.platform)
        self.add_widget(self.player)
        self.add_widget(self.invis_player)
        self.add_widget(self.obstacles)
        self.add_widget(self.invis_obstacles)
        
        self.score_board = Label(text = "0", font_name = 'assets/fonts/Futura Extra Black Condensed BT.ttf', 
                                 font_size = 60, center_x = self.width, center_y = self.height * 1.5, color = (.5, 0, .5))
        self.add_widget(self.score_board)
        
        Clock.schedule_interval(self.update, 1.0/60.0)
        
    def update(self, *ignores):
        if self._check_hit():
            self.player.trigger_death()
            print("Game Over!")
            return
        
        self.player.update()
        self.invis_player.update()
        self.platform.update()
        self.background.update()
        self.obstacles.update()
        self.invis_obstacles.update()
        
        self.score_board.text = str(self.obstacles.score)
        
    def _check_hit(self):
        condition1 = self.invis_player.collide_widget(self.obstacles.image)
        condition2 = self.invis_player.collide_widget(self.obstacles.image_dupe) 
        condition3 = self.invis_player.collide_widget(self.obstacles.image_dupe2)
        condition4 = self.invis_player.collide_widget(self.obstacles.image_dupe3) 
        return condition1 or condition2 or condition3 or condition4
    
    def _game_over(self):
        return
    
        
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
    
    
    
    
    