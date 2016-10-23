
from kivy.uix.widget import Widget

from sprite import Sprite

class Obstacles(Widget):
    def __init__(self, source):
        super(Obstacles, self).__init__()
        self.score = 0
        self.image = Sprite(source = source, x = 1200, y = 50)
        self.add_widget(self.image)
        self.size = self.image.size
        self.image_dupe = Sprite(source = source, x = 1400, y = 50)
        self.add_widget(self.image_dupe)
        self.image_dupe2 = Sprite(source = source, x = 1800, y = 50)
        self.add_widget(self.image_dupe2)
        self.image_dupe3 = Sprite(source = source, x = 2000, y = 50)
        self.add_widget(self.image_dupe3)

        
    def update(self):
        self.image.x -= 4
        self.image_dupe.x -= 4
        self.image_dupe2.x -= 4
        self.image_dupe3.x -= 4
        
        if self.image.right <= 60:
            self.image.x = 120 * 10
            self.score += 1
        if self.image_dupe.right <= 60:
            self.image_dupe.x = 140 * 10
            self.score += 1
        if self.image_dupe2.right <= 60:
            self.image_dupe2.x = 180 * 10
            self.score += 1
        if self.image_dupe3.right <= 60:
            self.image_dupe3.x = 200 * 10
            self.score += 1
        