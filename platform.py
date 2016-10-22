
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
        
    def update(self):
        self.image.x -= 8
        self.image_dupe.x -= 8
        
        if self.image.right <= 0:
            self.image.x = 0
            self.image_dupe.x = self.width