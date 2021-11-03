import os

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.lang.builder import Builder


class LoadFileExplorer(FileChooserIconView):
    filters = ['*.csv']

    def __init__(self, **kwargs):
        self.path = os.getcwd()
        super(LoadFileExplorer, self).__init__(**kwargs)


class LoadScreen(BoxLayout):
    def __init__(self, **kwargs):
        self.filepath = ''
        super(LoadScreen, self).__init__(**kwargs)

    def load(self, path, file):
        self.filepath = os.path.join(path, file[0])
        print(self.filepath)

    def cancel(self):
        pass


class LoadScreenApp(App):
    def build(self):
        return Builder.load_file('load_screen.kv')


if __name__ == '__main__':
    LoadScreenApp().run()