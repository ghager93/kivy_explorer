import os

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView, FileChooserListView


class LoadFileExplorer(FileChooserIconView):
    filters = ['*.csv']

    def __init__(self, **kwargs):
        self.path = os.getcwd()
        super(LoadFileExplorer, self).__init__(**kwargs)

    def load(self):
        pass


class LoadScreenApp(App):
    def build(self):
        return LoadFileExplorer()


if __name__ == '__main__':
    LoadScreenApp().run()