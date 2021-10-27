import os

from kivy.uix.filechooser import FileChooserListView


class Filechooser(FileChooserListView):
    dirselect = True

    def __get_directory_from_selection(self):
        if self.selection:
            if os.path.isdir(self.selection[0]):
                return self.selection[0]
            else:
                return os.path.dirname(self.selection[0])
        else:
            return ''

    @staticmethod
    def __dir_files(dir):
        if len(dir):
            return os.listdir(dir)
        else:
            return []
