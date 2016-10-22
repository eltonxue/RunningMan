from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock

running_anim = {x:'assets/player_running/resized75/running{}t.gif'.format(str(x))   for x in range(0,10)}
jump_anim = {x:'assets/player_running/jump/jump{}.gif'.format(str(x))   for x in range(0,7)}

class Sprite(Image):
    def __init__(self,**kwargs):
        super(Sprite,self).__init__(**kwargs)
        self.size = self.texture_size
        
        
class Player(Sprite):
    def __init__(self,pos):
        
        super(Player,self).__init__(source = running_anim[0], pos=pos)
        self._init_pos = pos[1]
        self._gravity = -.3
        self._velocity_y = 0
        self._run_count = 0
        self._jumped_count = 0
        self._jumped = False
    
    
    def on_touch_down(self, *ignore):
        if self._jumped == False:
            self._velocity_y = 5
            self._jumped = True
        else:
            pass
    
    def update(self):
        
        if self._jumped == True:
            
            self._velocity_y += self._gravity
            self.y += self._velocity_y
            
            self.source = jump_anim[self._jumped_count]
            
            self._jumped_count +=1
            
            if self._jumped_count > len(jump_anim)-1:
                self._jumped_count = 0
            
        if self.y <= self._init_pos:
            
            self._jumped = False
            self.y = self._init_pos
        
        if self._jumped == False:
               
            self._run_count+=1
        
            if self._run_count > len(running_anim) - 1:
                self._run_count = 0
            
            self.source = running_anim[self._run_count] 
# class Game(Widget):
#     
#     def __init__(self, **kwargs):
#         
#         super(Game,self).__init__(**kwargs)
#               
#         self.player = Player(pos =(20,self.height/2))
#       
#         
#         self.add_widget(self.player)
#         Clock.schedule_interval(self.update,2.0/60.0)
#         
#     def update(self, *ignore):
#         self.player.update()
        
#class SimpleWindow(App):
    #def build(self):
        #return Game(size = [1600*.35,900*.35])
    
#if __name__ == '__main__':
    #SimpleWindow().run()