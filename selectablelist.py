from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior


# Builder.load_file('selectablelist.kv')
Builder.load_string('''
<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
<SelectableList>:
    viewclass: 'SelectableLabel'
    
    item_default_size: None, dp(20)
    item_default_size_hint: 0.75, None
    item_size_hint_y: None
    
    SelectableRecycleBoxLayout:
        default_size: root.item_default_size
        default_size_hint: root.item_default_size_hint
        size_hint_y: root.item_size_hint_y
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True
''')

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


class SelectableList(RecycleView):
    def __init__(self, **kwargs):
        super(SelectableList, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(3)]

    def update_data(self, data):
        self.data = [{'text': str(d)} for d in data]


class SL(App):
    def build(self):
        return SelectableList()


if __name__ == '__main__':
    SL().run()