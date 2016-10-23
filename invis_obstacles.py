
from kivy.uix.widget import Widget

from sprite import Sprite

class InvisObstacles(Widget):
    def __init__(self, source):
        super(InvisObstacles, self).__init__()
        self.image = Sprite(source = source, x = 1200, y = 50)
        self.add_widget(self.image)
        self.size = self.image.size
        self.image_dupe = Sprite(source = source, x = 1400, y = 50)
        self.add_widget(self.image_dupe)
        self.image_dupe2 = Sprite(source = source, x = 1800, y = 50)
        self.add_widget(self.image_dupe2)
        self.image_dupe3 = Sprite(source = source, x = 2000, y = 50)
        self.add_widget(self.image_dupe3)
        
        self.change = 3

        
    def update(self):
        self.image.x -= self.change
        self.image_dupe.x -= self.change
        self.image_dupe2.x -= self.change
        self.image_dupe3.x -= self.change
        
        if self.image.right <= 0:
            self.image.x = 1200 - 60
        if self.image_dupe.right <= 0:
            self.image_dupe.x = 1400 - 60
        if self.image_dupe2.right <= 0:
            self.image_dupe2.x = 1800- 60
        if self.image_dupe3.right <= 0:
            self.image_dupe3.x = 2000 - 60
        