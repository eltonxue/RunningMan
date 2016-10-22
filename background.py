'''
Created on Oct 22, 2016

@author: EltonXue
'''

from kivy.uix.widget import Widget

from sprite import Sprite

class Background(Widget):
    def __init__(self, source):
        super(Background, self).__init__()
        self.image = Sprite(source = source)
        self.add_widget(self.image)
        self.size = self.image.size
        self.image_dupe = Sprite(source = source, x = self.width)
        self.add_widget(self.image_dupe)
        self.image_dupe2 = Sprite(source = source, x = self.width * 2)
        self.add_widget(self.image_dupe2)
        
    def update(self):
        self.image.x -= 1
        self.image_dupe.x -= 1
        self.image_dupe2.x -= 1
        
        if self.image.right <= 0:
            self.image.x = 0
            self.image_dupe.x = self.width
            self.image_dupe2.x = self.width * 2