from kivy.core.audio.audio_sdl2 import SoundSDL2
from sprite import Sprite
from kivy.core.audio import SoundLoader

sfx_jump = SoundSDL2(source = 'assets/sound_effects/jump11.wav')
sfx_fall = SoundSDL2(source = 'assets/sound_effects/fall.wav')

running_anim = 'assets/player_running/running_anim3.gif'
backflip_anim = 'assets/player_running/jump_anim2.gif'
death_anim = 'assets/player_running/death_anim.gif'
class Player(Sprite):
    def __init__(self,pos):
        
        super(Player,self).__init__(source = running_anim, pos=pos,anim_delay = 0.02,keep_data = True)
        self._init_pos = pos[1]
        self._gravity = -.3
        self._velocity_y = 0
  
        
        self._jumped = False
    
    
    def on_touch_down(self, *ignore):
        
        if self._jumped == False:
            sfx_jump.play()
            self._velocity_y = 10

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
            
        if self.y + 10 <= self._init_pos:
             
            self._jumped = False
            self.y = self._init_pos
            
        
        if self._jumped == False:
            self.anim_loop = 0
            self.source = running_anim

    def increase_speed(self):
        if self.anim_delay > 0:
            self.anim_delay -= 0.000001
            
        
    
    def trigger_death(self):
        sfx_fall.play()
        
        self.source = death_anim
        self.anim_loop = 1
    
    def sound_stop(self):
        return True
        
        
