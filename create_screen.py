import os

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.lang import Builder

from selectablelist import SelectableList

from util import pathfile

class FileExplorer(FileChooserListView):
    filters = ['*' + ext for ext in pathfile.AUDIO_EXTS]
    path = 'C://Users/ghage/Downloads/'

    def on_selection(self, *args):
        print(self.selection[0])
        if os.path.isdir(self.selection[0]):
            print([f for f in os.listdir(self.selection[0])
                   if os.path.splitext(f)[1] in pathfile.AUDIO_EXTS])


class LibraryList(SelectableList):
    def __init__(self, **kwargs):
        super(LibraryList, self).__init__(**kwargs)

    def append_all_audio_from_dir(self, dir):
        self.append_data(pathfile.audio_paths_in_dir(dir))



class CreateScreen(BoxLayout):
    def add_to_library(self):
        selection = self.ids.explorer.selection
        if not selection:
            return

        if os.path.isdir(selection[0]):
            self.ids.librarylist.append_all_audio_from_dir(selection[0])
        else:
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
