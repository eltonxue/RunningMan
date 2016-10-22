'''
Created on Oct 22, 2016

@author: EltonXue
'''


from kivy.uix.widget import Widget

from sprite import Sprite
from random import randint

class Obstacles(Widget):
    def __init__(self, source):
        super(Obstacles, self).__init__()
        self.image = Sprite(source = source, x = self.width * 30, y = 50)
        self.add_widget(self.image)
        self.size = self.image.size
        self.image_dupe = Sprite(source = source, x = self.width * 44, y = 50)
        self.add_widget(self.image_dupe)
        self.image_dupe2 = Sprite(source = source, x = self.width * 52, y = 50)
        self.add_widget(self.image_dupe2)
        self.image_dupe3 = Sprite(source = source, x = self.width * 76, y = 50)
        self.add_widget(self.image_dupe3)
        
    def update(self):
        self.image.x -= 4
        self.image_dupe.x -= 4
        self.image_dupe2.x -= 4
        self.image_dupe3.x -= 4
        
        if self.image.right <= 0 - self.width:
            self.image.x = self.width * 44
        if self.image_dupe.right <= 0 - self.width:
            self.image_dupe.x = self.width * 52
        if self.image_dupe2.right <= 0 - self.width:
            self.image_dupe2.x = self.width * 64
        if self.image_dupe3.right <= 0 - self.width:
            self.image_dupe3.x = self.width * 80
        