from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder


Builder.load_file('home_screen.kv')


class HomeScreen(Screen):
    pass


class HomeApp(App):
    def build(self):
        return HomeScreen()


if __name__ == '__main__':
    HomeApp().run()