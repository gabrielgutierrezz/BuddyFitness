from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button

class WelcomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        #green background

        with self.canvas.before:
            Color(0.749, 0.890, 0.706, 1) #green color
            self.rect= Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)
            

        label = Label(text='BuddyFitness', color=(1,1,1,1), font_size=60)
        
        #add label to box layout
        self.add_widget(label)
    def update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size