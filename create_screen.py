from kivy.app import App

from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.filechooser import FileChooserListView

from kivy.lang import Builder


from kivy.core.text import Label
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.lang import Builder

from selectablelist import SelectableList




class FileExplorer(FileChooserListView):
    def on_selection(self, *args):
        print(args)


class LibraryList(SelectableList):
    def __init__(self, **kwargs):
        super(LibraryList, self).__init__(**kwargs)


class CreateScreen(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        kv = Builder.load_file('create_screen.kv')
        return kv

    def on_start(self):
        self.root.ids.librarylist.update_data(['hello', 'goodbye'])
        self.root.ids.librarylist.default_size = None, 24
        print(self.root.ids.librarylist.children[0].default_size)


if __name__ == '__main__':
    MainApp().run()
