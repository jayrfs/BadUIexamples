from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder
Config.set('graphics', 'resizable', False)
Window.size = (360, 640)

class DOB(MDApp):
    def build(self):
        Builder.load_file('resources/dob.kv')
        return


if __name__ == '__main__':
    DOB().run()