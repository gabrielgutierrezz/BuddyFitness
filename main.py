#APP IDEA



from kivy.app import App

from welcomeScreen import WelcomeScreen
from homeScreen import HomePage



class MyApp(App):
    def build(self):
        return HomePage()
    
if __name__ == '__main__':
    MyApp().run()