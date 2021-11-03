from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang.builder import Builder

from home_screen import HomeScreen
from create_screen import CreateScreen
from load_screen import LoadScreen


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(CreateScreen(name='create'))
        sm.add_widget(LoadScreen(name='load'))

        return sm

    def on_start(self):
        print(self.root.children[0])

if __name__ == '__main__':
    MyApp().run()
