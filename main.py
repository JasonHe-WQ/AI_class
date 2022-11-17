import csv_reader
import linear_process


class read_csv():

    def __init__(self):
        self.data_x = None
        self.data_y = None
        self.filename = None

    @property
    def load_filename(self):
        self.filename = 'kc_house_data.csv'
        return self.filename

    @load_filename.setter
    def load_filename(self, name):
        self.filename = name

    @staticmethod
    def describe():
        print('这个类负责读取csv文件，可以通过方法load_filename重新设置文件名')

    def read(self):
        if not (self.data_x or self.data_y):
            self._read_csv()

    def _read_csv(self, name='kc_house_data.csv'):
        self.data_x, self.data_y = csv_reader.read_csv(name)


class process_data():
    def __init__(self, data):
        self.data = data

    def process(self):
        processed_data = linear_process.process(self.data)


class display_data():

    def __init__(self, data):
        self.data = data

    def display(self):
        pass


a = read_csv()
print(a.load_filename)
a.read()
a.describe()
print(a.data_x)
