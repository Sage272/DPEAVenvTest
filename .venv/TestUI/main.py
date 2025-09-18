import os
os.environ["DISPLAY"] = ":0.0"
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivy.core.window import Window
from faker import Faker
import DPEAButton

class MyApp(App):
    def build(self):
        return sm

sm = ScreenManager()
Builder.load_file('main.kv')
Window.clearcolor = (0.5, 0.5, 0.5, 1) # (DARK GRAY)

class MainScreen(Screen):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

    expanded = False
    def generate(self):
        if not self.expanded:
            prev_center_x = self.ids.data.center_x
            size_up = Animation(width = self.ids.data.width + 200, center_x = prev_center_x, duration=0.5, t='linear')
            size_up.bind(on_complete=self.gen_text)
            size_up.start(self.ids.data)
            self.expanded = True
            #stufffffff
        else:
            self.gen_text()

    def gen_text(self, animation=None, widget=None):
        faker = Faker()
        self.ids.text1.text = str(faker.date_of_birth())
        self.ids.text2.text = str(faker.license_plate())
        self.ids.data.text = faker.name() + "\n" + faker.address() + "\n" + str(faker.phone_number())
    
    def quit(self):
        print("Exit")
        MyApp().stop()

sm.add_widget(MainScreen(name = 'main'))

# ////////////////////////////////////////////////////////////////
# //                          RUN APP                           //
# ////////////////////////////////////////////////////////////////
if __name__ == "__main__":
    MyApp().run()
