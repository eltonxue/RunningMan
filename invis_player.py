
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import *


running_anim = {x:'assets/player_running/resized75/running{}t.gif'.format(str(x))   for x in range(0,10)}
jump_anim = {x:'assets/player_running/jump/jump{}.gif'.format(str(x))   for x in range(0,7)}

class Sprite(Image):
    def __init__(self,**kwargs):
        super(Sprite,self).__init__(**kwargs)
        self.size = self.texture_size
        
        
class InvisPlayer(Widget):
    def __init__(self,pos):
        super(InvisPlayer, self).__init__()
        self._pos = pos
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
            
            print(self.size)
            print(self.pos)
            self.source = jump_anim[self._jumped_count]
            
            self._jumped_count +=1
            
            if self._jumped_count > len(jump_anim)-1:
                self._jumped_count = 0
            
        if self.y <= self._init_pos:
            
            self._jumped = False
            self.y = self._init_pos
            print(self.size)
            print(self.pos)
            print('-------')
        
        if self._jumped == False:
               
            self._run_count+=1
        
            if self._run_count > len(running_anim) - 1:
                self._run_count = 0
            
            self.source = running_anim[self._run_count] 
