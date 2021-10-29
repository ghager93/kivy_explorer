from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.lang import Builder

from selectablelist import SelectableList
from util.pathfile import AUDIO_EXTS

class FileExplorer(FileChooserListView):
    filters = ['*' + ext for ext in AUDIO_EXTS]
    def on_selection(self, *args):
        print(args)


class LibraryList(SelectableList):
    def __init__(self, **kwargs):
        super(LibraryList, self).__init__(**kwargs)


class CreateScreen(BoxLayout):
    def add_to_library(self):
        selection = self.ids.explorer.selection
        if selection:
            self.ids.librarylist.append_data(selection[0])

    def clear_library(self):
        self.ids.librarylist.clear_data()


class MainApp(App):
    def build(self):
        kv = Builder.load_file('create_screen.kv')
        return kv

    def on_start(self):
        self.root.ids.librarylist.replace_data([n for n in range(40)])


if __name__ == '__main__':
    MainApp().run()
