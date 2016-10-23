
from kivy.uix.widget import Widget

from sprite import Sprite

class Platform(Widget):
    def __init__(self, source):
        super(Platform, self).__init__()
        self.image = Sprite(source = source)
        self.add_widget(self.image)
        self.size = self.image.size
        self.image_dupe = Sprite(source = source, x = self.width)
        self.add_widget(self.image_dupe)
        self.image_dupe2 = Sprite(source = source, x = self.width * 2)
        self.add_widget(self.image_dupe2)
        self.image_dupe3 = Sprite(source = source, x = self.width * 3)
        self.add_widget(self.image_dupe3)
        
        self.change = 4
     
    def update(self):
        self.image.x -= self.change
        self.image_dupe.x -= self.change
        self.image_dupe2.x -= self.change
        self.image_dupe3.x -= self.change
        
        if self.image.right <= 0:
            self.image.x = 0
            self.image_dupe.x = self.width
            self.image_dupe2.x = self.width * 2
            self.image_dupe3.x = self.width * 3