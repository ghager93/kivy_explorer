import os

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.stacklayout import StackLayout
from kivy.lang import Builder

from selectablelist import SelectableList
from util import pathfile
from library import Library


class OverwritePopup(Popup):
    def save_and_dismiss(self):
        self.save_func()
        self.dismiss()


class PopupStack(StackLayout):
    pass


class FileExplorer(FileChooserListView):
    filters = ['*' + ext for ext in pathfile.AUDIO_EXTS]
    path = 'C://Users/ghage/Downloads/'


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


class CreateScreen(BoxLayout):
    save_dir = 'C://Users/ghage/PycharmProjects/kivy_explorer/lib/user/'

    def __init__(self, **kwargs):
        super(CreateScreen, self).__init__(**kwargs)
        self.library = Library()
        self.overwrite_popup = OverwritePopup()
        self.overwrite_popup.save_func = self.save_data

    def add_to_library(self):
        """
        If the selection is a directory, add all audio files from that directory.
        If the selection is a file, just add the file.
        """
        selection = self.ids.explorer.selection
        if selection:
            if os.path.isdir(selection[0]):
                self._add_dir_to_library(selection[0])
            else:
                self.library.append(selection[0])
            self._update_list()

    def _add_dir_to_library(self, dir):
        self.library.append(pathfile.audio_paths_in_dir(dir))

    def remove_selected(self):
        self.library.remove(self.ids.librarylist.selected_indices)
        self._update_list()

    def clear_library(self):
        self.library.clear()
        self._update_list()

    def _update_list(self):
        if (self.ids.fullpath_check.active):
            self.ids.librarylist.replace_data(
                self.library.data['path'].to_list())
        else:
            self.ids.librarylist.replace_data(
                self.library.data['path_short'].to_list())

    def save_library(self):
        if os.path.exists(self.get_save_path()):
            self.overwrite_popup.open()
        else:
            self.save_data()

    def save_data(self):
        self.library.save(self.get_save_path())

    def get_save_path(self):
        return os.path.join(self.save_dir,
                            self.ids.name_input.text + '.csv')


class MainApp(App):
    def build(self):
        return Builder.load_file('create_screen.kv')


if __name__ == '__main__':
    MainApp().run()
