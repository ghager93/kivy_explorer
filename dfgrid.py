import os
import pandas as pd

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder


Builder.load_file('dfgrid.kv')


class DfElement(Label):
    pass


class DfGrid(GridLayout):
    def __init__(self, **kwargs):
        super(DfGrid, self).__init__(**kwargs)

    def show(self, df: pd.DataFrame):
        self.cols = df.shape[1]
        for column in df.columns:
            background_color = 0, 0, 0, 0.3
            dfe = DfElement(text=str(column))
            dfe.background_color = background_color
            self.add_widget(dfe)

        for i, row in enumerate(df.iterrows()):
            if i % 2:
                background_color = 0, 0, 0, 0.1
            else:
                background_color = 0, 0, 0, 0
            for element in row[1]:
                self.add_widget(DfElement(text=str(element),
                                          background_color=background_color))


class DfScroll(ScrollView):
    def __init__(self, **kwargs):
        super(DfScroll, self).__init__(**kwargs)
        self.add_widget(DfGrid())

    def show(self, df: pd.DataFrame):
        self.children[0].show(df)


class DfApp(App):
    def build(self):
        dfs = DfScroll()
        return dfs

    def on_start(self):
        self.root.children[0].show(
            pd.read_csv(r'C:\Users\ghage\PycharmProjects\kivy_explorer\lib\user\testlong.csv'))


if __name__ == '__main__':
    DfApp().run()

