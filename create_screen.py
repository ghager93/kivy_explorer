import os
import pandas as pd
import re
import time

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

    def add_selection(self, selection):
        if os.path.isdir(selection):
            self._append_all_audio_from_dir(selection)
        else:
            self.append_data(selection)

    def _append_all_audio_from_dir(self, dir):
        self.append_data(pathfile.audio_paths_in_dir(dir))


class Library:
    data_columns = ['path', 'path_short', 'time_added']
    shortening_pattern = re.compile(r'[^\/\\]+$')

    def __init__(self):
        self.data = pd.DataFrame(columns=self.data_columns)

    def _add_element(self, element):
        element = str(element)
        if element not in self.data['path'].values:
            shortened_path = self.shortening_pattern.search(element)[0]
            time_added = time.time()

            self.data = self.data.append({'path': element,
                                          'path_short': shortened_path,
                                          'time_added': time_added},
                                         ignore_index=True)

    def append(self, data):
        if type(data) is list:
            [self._add_element(d) for d in data]
        else:
            self._add_element(data)

    def remove(self, indices):
        self.data = self.data.drop(indices)

    def clear(self):
        self.data = pd.DataFrame(columns=self.data_columns)

    def print(self):
        print(self.data.head())



class CreateScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(CreateScreen, self).__init__(**kwargs)
        self.library = Library()

    def add_to_library(self):
        """
        If the selection is a directory, add all audio files from that directory.
        If the selection is a file, just add the file.
        """
        selection = self.ids.explorer.selection
        if selection:
            self.ids.librarylist.add_selection(selection[0])

    def add_to_libobj(self):
        selection = self.ids.explorer.selection
        if selection:
            self.library.append(selection[0])
            self._update_list()

    def remove_selected(self):
        self.library.remove(self.ids.librarylist.selected_indices)
        self._update_list()

    def clear_library(self):
        self.ids.librarylist.clear_data()

    def _update_list(self):
        self.ids.librarylist.replace_data(self.library.data['path'].to_list())


class MainApp(App):
    def build(self):
        kv = Builder.load_file('create_screen.kv')
        return kv

    def on_start(self):
        self.root.ids.librarylist.replace_data([n for n in range(40)])


if __name__ == '__main__':
    MainApp().run()
