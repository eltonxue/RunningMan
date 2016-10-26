
from kivy.uix.widget import Widget


running_anim = 'assets/player_running/running_anim3.gif'
backflip_anim = 'assets/player_running/jump_anim2.gif'
        
class InvisPlayer(Widget):
    def __init__(self, pos):
        super(InvisPlayer, self).__init__()
        self._pos = pos
        self._init_pos = pos[1]
        self._gravity = -.3
        self._velocity_y = 0
        
        self._jumped = False
        self.source = running_anim
        self.anim_delay = 0.02
    
    
    def on_touch_down(self, *ignore):
        
        if self._jumped == False:
            self._velocity_y = 7
            self._jumped = True
        else:
            pass
    
    def update(self):
        
        if self._jumped == True:
            
            self._velocity_y += self._gravity
            self.y += self._velocity_y
            
            self.source = backflip_anim
            self.anim_loop = 1
          
            
        if self.y <= self._init_pos:
            
            self._jumped = False
            self.y = self._init_pos
        
        if self._jumped == False:
               

            
            self.source = running_anim
    
    def increase_speed(self):
        if self.anim_delay > 0:
            self.anim_delay -= 0.000001
