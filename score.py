from kivy.app import App

from kivy.uix.label import Label


class RunningMan(App):
    def build(self):
        
        return Label(font_name = 'assets/fonts/Futura Extra Black Condensed BT.ttf', text = "14", font_size = 50,
                     color = (1,1,1))
        
if __name__ == '__main__':
        
    RunningMan().run()       