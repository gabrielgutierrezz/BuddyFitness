# home_page.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.anchorlayout import AnchorLayout

green =[0.3529, 0.8549, 0.5255, 1]

class HomePage(BoxLayout):
    def build(self):
        #this will be the ultimate box which will serve as the base box technicallly for all my widgets
        superBox=BoxLayout(orientation = 'vertical')
        
        #the box that will be all of superbox

        # calling this makes widget horizontal

        horizontalBox = BoxLayout(orientation = 'horizontal')

        #layout to center

        anchorLayout = AnchorLayout(anchor_x= 'center', anchor_y = 'top')

        #buttons that will be placed in the horizontal box

        headerButton = Button(text = 'BuddyFitness')

        anchorLayout.add_widget(headerButton)