import os

from kivy.app import App
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.uix.filechooser import FileChooserListView
from kivy.properties import ObjectProperty, BooleanProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.lang import Builder

from util import pathfile


Builder.load_file('editor.kv')


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected


class Explorer(FileChooserListView):
    dirselect = True

    def on_selection(self, *args):
        print(self.selection)

        App.get_running_app().root.dir_path = self.__get_directory_from_selection()

        App.get_running_app().root.ids.rv.update_data(
            pathfile.filter_for_audio(
                self.__dir_files(App.get_running_app().root.dir_path)))

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


class DirList(RecycleView):
    def __init__(self, **kwargs):
        super(DirList, self).__init__(**kwargs)
        self.data = [{'text': 'hello'}]

    def update_data(self, data):
        self.data = [{'text': str(d)} for d in data]


class SelectButton(Button):
    def on_press(self):
        print(App.get_running_app().root.dir_path)


class Root(BoxLayout):
    dir_path = StringProperty('')

    filechooser = Explorer()


class Editor(App):
    def build(self):
        self.root.ids.filechooser.bind(on_selection=self.root.ids.rv.update_data)

if __name__ == '__main__':
    Editor().run()
