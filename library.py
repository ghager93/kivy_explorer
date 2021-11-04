import pandas as pd
import re
import time


class Library:
    data_columns = ['path', 'path_short', 'time_added']
    shortening_pattern = re.compile(r'[^\/\\]+$')

    def __init__(self, data=None):
        if data:
            self.data = data
        else:
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

    def save(self, path):
        self.data.to_csv(path, index=False)


def read_csv(path):
    return Library(pd.read_csv(path))



