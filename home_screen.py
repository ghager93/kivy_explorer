from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder


class HomeScreen(BoxLayout):
    pass


class HomeApp(App):
    def build(self):
        return Builder.load_file('home_screen.kv')


if __name__ == '__main__':
    HomeApp().run()