from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.config import Config
from kivy.lang import Builder
Config.set('graphics', 'resizeable', 0)
Window.size = (375,700)

class MainScreen(Screen): #mainscreen inside your scrollview
    pass
class FirstScreen(Screen):#first screen
    pass

class SecondScreen(Screen): #second screen
    pass

root = Builder.load_file("main.kv") #should match the name of your kv file

class myapp(App):
    def build(self):
        return root

if __name__ == '__main__':
    myapp().run()
