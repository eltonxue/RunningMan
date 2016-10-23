
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

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class StartScreen(Screen):
    pass

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.game = Game()
        self.add_widget(self.game)

class SettingsScreen(Screen):
#     def __init__(self):
#         super(SettingsScreen, self).__init__()
#          
#         self.music_label = Label(text = "Music:")
#         self.music_button = Button(text = "ON") 
#          
#     def build(self):
#         self.music_button.bind(on_press = self.clk)
#         layout = BoxLayout()
#         layout.orientation = 'vertical'
#         layout.add_widget(self.music_button)
#         layout.add_widget(self.music_label)
#          
#         return layout
#      
#     def clk(self, obj):
#         print("changed")
#         self.label_button.text = "OFF"
#     def __init__(self, **kwargs):
#         super(SettingsScreen, self).__init__(**kwargs)
#         self.music_on_off = "Music: ON"
    music_on_off = "Music: ON"
     
    def music_toggle(self):
        if self.music_on_off == "Music: ON":
            self.music_on_off = "Music: OFF"
        else:
            self.music_on_off = "Music: ON"
#         

class CreditsScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
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
    
        self.score_label = Label(text = "Score: ", font_name = 'assets/fonts/Futura Extra Black Condensed BT.ttf', 
                                 font_size = 20, center_x = 50, center_y = self.platform.height/2 + 5, color = (0.0,0.0,0.0,1))
        self.score_board = Label(text = "0", font_name = 'assets/fonts/Futura Extra Black Condensed BT.ttf', 
                                 font_size = 30, center_x = 100, center_y = self.platform.height/2 + 5)
        self.add_widget(self.score_label)
        self.add_widget(self.score_board)
        
        self.start_game = False
        
        Clock.schedule_interval(self.update, 1.0/60.0)
    
    def on_touch_up(self,touch):
        self.start_game = True
        
    def update(self, *ignores):
        if self._check_hit():
            self.player.trigger_death()
            print("Game Over!")
            return
        
        if self.start_game == True:
            self.player.update()
            self.invis_player.update()
            self.platform.update()
            self.background.update()
            self.obstacles.update()
            self.invis_obstacles.update()
            
            self.score_board.text = str(self.obstacles.score)
            
            if self.obstacles.score != 0 and self.obstacles.score % 10 == 0:
                self.platform.change += .002
                self.obstacles.change += .002
                self.invis_obstacles.change += .002
                
        
    def _check_hit(self):
        condition1 = self.invis_player.collide_widget(self.obstacles.image)
        condition2 = self.invis_player.collide_widget(self.obstacles.image_dupe) 
        condition3 = self.invis_player.collide_widget(self.obstacles.image_dupe2)
        condition4 = self.invis_player.collide_widget(self.obstacles.image_dupe3) 
        return condition1 or condition2 or condition3 or condition4
    
    def _game_over(self):
        return
    
presentation = Builder.load_file("main.kv") 
        
class RunningMan(App):
    def build(self):
        Window.size = [1600 * .25, 900 * .25]
        return presentation
    
    def update(self, *ignore):
        self.platform.update()
        self.background.update()
        self.obstacles.update()
        self.invis_obstacles.update()
            
if __name__ == "__main__":
    RunningMan().run()
    
    
    
    
    