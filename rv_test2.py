from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

from selectablelist import SelectableList


class MyList(SelectableList):
    def __init__(self, **kwargs):
        super(MyList, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.cnt = 0
        self.nums = []

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'c':
            self.nums.append(self.cnt)
            self.cnt += 1
            self.replace_data(self.nums)
        return True


class MyApp(App):
    def build(self):
        return MyList()


if __name__ == '__main__':
    MyApp().run()

