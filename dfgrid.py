import os
import pandas as pd

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
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
            self.add_widget(DfElement(text=column))

        for row in df.iterrows():
            for element in row[1]:
                self.add_widget(DfElement(text=str(element)))


class DfScroll(ScrollView):
    pass


class DfApp(App):
    def build(self):
        dfs = DfScroll()
        dfs.add_widget(DfGrid())
        return dfs

    def on_start(self):
        self.root.children[0].show(
            pd.read_csv(r'C:\Users\ghage\PycharmProjects\kivy_explorer\lib\user\testlong.csv'))


if __name__ == '__main__':
    DfApp().run()

