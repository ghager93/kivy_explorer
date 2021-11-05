import pandas as pd

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

import library

from dfgrid import DfScroll


class ViewScreen(BoxLayout):
    def __init__(self, csv_path, **kwargs):
        super(ViewScreen, self).__init__(**kwargs)
        self.csv_path = csv_path
        self.add_widget(DfScroll())

    def data(self):
        self.children[0].show(pd.read_csv(self.csv_path))

class ViewApp(App):
    def build(self):
        return ViewScreen(r'C:\Users\ghage\PycharmProjects\kivy_explorer\lib\user\test.csv')

    def on_start(self):
        self.root.data()


if __name__ == '__main__':
    ViewApp().run()
